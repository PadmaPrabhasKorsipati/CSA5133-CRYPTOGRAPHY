import socket
import threading

from network import NetworkProtocol

HOST = "0.0.0.0"
PORT = 5000

clients = {}
lock = threading.Lock()

# Store latest handshake packets
hello_packets = {}
pubkey_packets = {}
ready_packets = {}


def send_to_other(sender_socket, packet):
    """
    Forward packet to the other connected client.
    """

    with lock:

        for client in clients:

            if client != sender_socket:

                try:
                    NetworkProtocol.send_packet(client, packet)

                except Exception as e:
                    print(f"[ERROR] Forward Failed : {e}")


def handle_client(client_socket, address):

    username = "Unknown"

    print(f"\n[CONNECTED] {address}")

    try:

        while True:

            packet = NetworkProtocol.receive_packet(client_socket)

            if packet is None:
                break

            packet_type = packet.get("type")

            # -----------------------------
            # HELLO
            # -----------------------------
            if packet_type == "HELLO":

                username = packet["username"]

                with lock:
                  clients[client_socket] = username
                  hello_packets[username] = packet

                print(f"[HELLO] {username}")

                send_to_other(client_socket, packet)

               # Send stored HELLO packets from existing clients

                with lock:
                   for user, hello in hello_packets.items():
                       if user != username:
                         NetworkProtocol.send_packet(client_socket, hello)

            # Send stored public keys
                   for user, pub in pubkey_packets.items():
                      if user != username:
                       NetworkProtocol.send_packet(client_socket, pub)

        # Send stored READY packets
                   for user, ready in ready_packets.items():
                     if user != username:
                        NetworkProtocol.send_packet(client_socket, ready)
            
            # -----------------------------
            # PUBLIC KEY
            # -----------------------------
            elif packet_type == "PUBKEY":

              with lock:
                 pubkey_packets[username] = packet

              print(f"[PUBKEY] {username}")

              send_to_other(client_socket, packet)
           

            # -----------------------------
            # READY
            # -----------------------------

            elif packet_type == "READY":

              with lock:
                ready_packets[username] = packet

              print(f"[READY] {username}")

              send_to_other(client_socket, packet)

            # -----------------------------
            # VOICE
            # -----------------------------

            elif packet_type == "VOICE":

                print(f"[VOICE] Packet from {username}")

                send_to_other(client_socket, packet)

            # -----------------------------
            # ACK
            # -----------------------------

            elif packet_type == "ACK":

                print(f"[ACK] {username}")

                send_to_other(client_socket, packet)

            # -----------------------------
            # EXIT
            # -----------------------------

            elif packet_type == "EXIT":

                print(f"[EXIT] {username}")

                send_to_other(client_socket, packet)

                break

            # -----------------------------
            # UNKNOWN
            # -----------------------------

            else:

                print(f"[UNKNOWN] {packet}")

    except Exception as e:

        print(f"[ERROR] {username} : {e}")

    finally:

        with lock:
           
           if client_socket in clients:

             user = clients[client_socket]

             del clients[client_socket]

             hello_packets.pop(user, None)
             pubkey_packets.pop(user, None)
             ready_packets.pop(user, None)


        client_socket.close()

        print(f"[DISCONNECTED] {username}")


def start_server():

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    server.bind((HOST, PORT))

    server.listen(2)

    print("=" * 60)
    print(" END-TO-END ENCRYPTED VOICE RELAY ")
    print("=" * 60)

    print(f"Listening on {HOST}:{PORT}")
    print("Waiting for Alice and Bob...\n")

    while True:

        client_socket, address = server.accept()

        with lock:

            if len(clients) >= 2:

                print("[INFO] Maximum 2 clients allowed.")

                client_socket.close()

                continue

        thread = threading.Thread(
            target=handle_client,
            args=(client_socket, address),
            daemon=True
        )

        thread.start()


if __name__ == "__main__":

    start_server()