from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    PublicFormat
)
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

import base64


class CryptoManager:

    def __init__(self):

        self.private_key = x25519.X25519PrivateKey.generate()

        self.public_key = self.private_key.public_key()

        self.session_key = None

    # ----------------------------
    # Public Key
    # ----------------------------

    def get_public_key_bytes(self):

        return self.public_key.public_bytes(
            encoding=Encoding.Raw,
            format=PublicFormat.Raw
        )

    # ----------------------------
    # Shared Secret
    # ----------------------------

    def derive_session_key(self, peer_public_key_bytes):

        peer_public = x25519.X25519PublicKey.from_public_bytes(
            peer_public_key_bytes
        )

        shared_secret = self.private_key.exchange(peer_public)

        hkdf = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b"voice-messenger"
        )

        self.session_key = hkdf.derive(shared_secret)

        return self.session_key

    # ----------------------------
    # Encrypt
    # ----------------------------

    def encrypt(self, plaintext):

        if self.session_key is None:
            raise ValueError("Session key not established")

        nonce = os.urandom(12)

        aes = AESGCM(self.session_key)

        ciphertext = aes.encrypt(
            nonce,
            plaintext,
            None
        )

        return nonce, ciphertext

    # ----------------------------
    # Decrypt
    # ----------------------------

    def decrypt(self, nonce, ciphertext):

        if self.session_key is None:
            raise ValueError("Session key not established")

        aes = AESGCM(self.session_key)

        plaintext = aes.decrypt(
            nonce,
            ciphertext,
            None
        )

        return plaintext

    def get_public_key_base64(self):
        """
        Returns the public key as a Base64 string for JSON transport.
        """
        return base64.b64encode(
            self.get_public_key_bytes()
        ).decode("utf-8")

    def derive_session_key_base64(self, peer_key_base64):
        """
        Accepts a Base64 public key string and derives the AES session key.
        """
        peer_bytes = base64.b64decode(peer_key_base64)

        return self.derive_session_key(peer_bytes)