import socket
import threading
import base64
import time

from network import NetworkProtocol
from crypto import CryptoManager
from audio import AudioManager
from config import HOST, PORT


class VoiceClient:

    # =========================================================
    # Constructor
    # =========================================================

    def __init__(self):

        # -----------------------------
        # Network
        # -----------------------------

        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        self.connected = False

        # -----------------------------
        # User
        # -----------------------------

        self.username = ""
        self.peer_name = ""

        # -----------------------------
        # Audio
        # -----------------------------

        self.audio = AudioManager()

        self.audio_data = None

        # -----------------------------
        # Cryptography
        # -----------------------------

        self.crypto = CryptoManager()

        # -----------------------------
        # Handshake
        # -----------------------------

        self.public_key_sent = False

        self.public_key_received = False

        self.ready_sent = False

        self.peer_ready = False

        self.secure_channel = False

        # -----------------------------
        # Synchronization
        # -----------------------------

        self.lock = threading.Lock()

        # -----------------------------
        # GUI Callbacks
        # -----------------------------

        self.on_log = None

        self.on_connected = None

        self.on_secure = None

        self.on_voice_received = None

        print("Voice Client Initialized")

    # =========================================================
    # Logger
    # =========================================================

    def log(self, message):

        print(message)

        if self.on_log:

            self.on_log(message)

    # =========================================================
    # Connect
    # =========================================================

    def connect(self):

        self.socket.connect(
            (HOST, PORT)
        )

        self.connected = True

        if self.on_connected:

            self.on_connected()

        self.log("Connected to Relay Server")

    # =========================================================
    # Send Packet
    # =========================================================

    def send_packet(self, packet):

        NetworkProtocol.send_packet(

            self.socket,

            packet

        )

    # =========================================================
    # HELLO
    # =========================================================

    def send_hello(self):

        packet = {

            "type": "HELLO",

            "username": self.username

        }

        self.send_packet(packet)

        self.log("HELLO Sent")

    # =========================================================
    # PUBLIC KEY
    # =========================================================

    def send_public_key(self):

        packet = {

            "type": "PUBKEY",

            "username": self.username,

            "public_key":

                self.crypto.get_public_key_base64()

        }

        self.send_packet(packet)

        self.public_key_sent = True

        self.log("Public Key Sent")

    # =========================================================
    # READY
    # =========================================================

    def send_ready(self):

        packet = {

            "type": "READY",

            "username": self.username

        }

        self.send_packet(packet)

        self.ready_sent = True

        self.log("READY Sent")

    # =========================================================
    # EXIT
    # =========================================================

    def send_exit(self):

        packet = {

            "type": "EXIT",

            "username": self.username

        }

        self.send_packet(packet)

    # =========================================================
    # Handle HELLO
    # =========================================================

    def handle_hello(self, packet):

        if packet["username"] == self.username:

            return

        self.peer_name = packet["username"]

        self.log(f"{self.peer_name} joined the chat.")

        # =========================================================
    # Handle Public Key
    # =========================================================

    def handle_pubkey(self, packet):

        if packet["username"] == self.username:
            return

        self.log("Received Peer Public Key")

        self.crypto.derive_session_key_base64(
            packet["public_key"]
        )

        self.public_key_received = True

        self.log("AES Session Key Generated")

        if not self.ready_sent:
            self.send_ready()

    # =========================================================
    # Handle READY
    # =========================================================

    def handle_ready(self, packet):

        if packet["username"] == self.username:
            return

        self.peer_ready = True

        if self.ready_sent and not self.secure_channel:

            self.secure_channel = True

            if self.on_secure:
                self.on_secure()

            self.log("================================")
            self.log("SECURE CHANNEL ESTABLISHED")
            self.log("================================")

    # =========================================================
    # Handle Incoming Voice
    # =========================================================

    def handle_voice(self, packet):

        if not self.secure_channel:

            self.log("Received voice before secure channel.")

            return

        self.log("Encrypted Voice Received")

        try:

            nonce = base64.b64decode(
                packet["nonce"]
            )

            ciphertext = base64.b64decode(
                packet["ciphertext"]
            )

            wav_bytes = self.crypto.decrypt(
                nonce,
                ciphertext
            )

            audio = self.audio.bytes_to_audio(
                wav_bytes
            )

            self.audio.save_received(
                wav_bytes
            )

            self.audio.play(audio)

            if self.on_voice_received:
                self.on_voice_received()

            ack = {

                "type": "ACK",

                "username": self.username

            }

            self.send_packet(ack)

        except Exception as e:

            print("Voice Decryption Error:", e)

    # =========================================================
    # Receive Loop
    # =========================================================

    def receive_loop(self):

        while self.connected:

            try:

                packet = NetworkProtocol.receive_packet(
                    self.socket
                )

                if packet is None:
                    break

                packet_type = packet.get("type")

                if packet_type == "HELLO":

                    self.handle_hello(packet)

                elif packet_type == "PUBKEY":

                    self.handle_pubkey(packet)

                elif packet_type == "READY":

                    self.handle_ready(packet)

                elif packet_type == "VOICE":

                    self.handle_voice(packet)

                elif packet_type == "ACK":

                    self.log("Voice Delivered Successfully")

                elif packet_type == "EXIT":

                    self.log("Peer Disconnected")

                    self.connected = False

                    break

                else:

                    self.log(f"Unknown Packet : {packet}")

            except Exception as e:

                print("Receive Error:", e)

                break

        self.connected = False

    # =========================================================
    # Record → Encrypt → Send Voice
    # =========================================================

    def send_voice(self):

        if not self.secure_channel:

            self.log("Secure channel not established.")

            return

        self.log("Recording Voice...")

        audio = self.audio.record(5)

        wav_bytes = self.audio.audio_to_bytes(audio)

        nonce, ciphertext = self.crypto.encrypt(
            wav_bytes
        )

        packet = {

            "type": "VOICE",

            "username": self.username,

            "nonce": base64.b64encode(
                nonce
            ).decode(),

            "ciphertext": base64.b64encode(
                ciphertext
            ).decode()

        }

        self.log("Encrypting Voice...")

        self.send_packet(packet)

        self.log("Encrypted Voice Sent")

        # =========================================================
    # Start Client
    # =========================================================

    def start(self, username):

        self.username = username

        self.connect()

        receiver = threading.Thread(
            target=self.receive_loop,
            daemon=True
        )

        receiver.start()

        time.sleep(1)

        self.send_hello()

        self.send_public_key()

        self.log("Waiting for secure channel...")

        while not self.secure_channel and self.connected:

            time.sleep(0.2)

        if not self.connected:

            self.log("Connection Lost")

            return

        self.log("===================================")
        self.log("Secure Voice Messaging Started")
        self.log("===================================")

        # GUI controls the client from now on
        while self.connected:

            time.sleep(0.2)

    # =========================================================
    # Record Voice
    # =========================================================

    def record_voice(self):

        if not self.secure_channel:

            self.log("Secure channel not established.")

            return False

        self.log("Recording Voice...")

        self.audio_data = self.audio.record(5)

        self.log("Recording Finished")

        return True

    # =========================================================
    # Send Recorded Voice
    # =========================================================

    def send_recorded_voice(self):

        if self.audio_data is None:

            self.log("No recorded voice available.")

            return False

        wav_bytes = self.audio.audio_to_bytes(
            self.audio_data
        )

        nonce, ciphertext = self.crypto.encrypt(
            wav_bytes
        )

        packet = {

            "type": "VOICE",

            "username": self.username,

            "nonce": base64.b64encode(
                nonce
            ).decode(),

            "ciphertext": base64.b64encode(
                ciphertext
            ).decode()

        }

        self.log("Encrypting Voice...")

        self.send_packet(packet)

        self.log("Encrypted Voice Sent")

        return True

    # =========================================================
    # Play Last Voice
    # =========================================================

    def play_last_voice(self):

        self.audio.play_last()

    # =========================================================
    # Disconnect
    # =========================================================

    def disconnect(self):

        if not self.connected:
            return

        try:

            self.send_exit()

        except:

            pass

        self.connected = False

        try:

            self.socket.close()

        except:

            pass

        self.log("Disconnected")