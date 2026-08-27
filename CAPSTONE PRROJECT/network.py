import json
import struct


class NetworkProtocol:
    """
    Handles sending and receiving JSON packets over TCP using
    a 4-byte length prefix.
    """

    HEADER_SIZE = 4

    @staticmethod
    def send_packet(sock, packet):
        """
        Send a JSON packet.
        """

        data = json.dumps(packet).encode("utf-8")

        length = struct.pack("!I", len(data))

        sock.sendall(length + data)

    @staticmethod
    def receive_exact(sock, size):
        """
        Receive exactly 'size' bytes.
        """

        buffer = b""

        while len(buffer) < size:

            chunk = sock.recv(size - len(buffer))

            if not chunk:
                return None

            buffer += chunk

        return buffer

    @staticmethod
    def receive_packet(sock):
        """
        Receive one complete JSON packet.
        """

        header = NetworkProtocol.receive_exact(
            sock,
            NetworkProtocol.HEADER_SIZE
        )

        if header is None:
            return None

        packet_length = struct.unpack("!I", header)[0]

        payload = NetworkProtocol.receive_exact(
            sock,
            packet_length
        )

        if payload is None:
            return None

        return json.loads(payload.decode("utf-8"))