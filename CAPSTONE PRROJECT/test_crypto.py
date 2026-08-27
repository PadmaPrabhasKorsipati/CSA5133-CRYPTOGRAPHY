from crypto import CryptoManager

alice = CryptoManager()
bob = CryptoManager()

# Exchange public keys
alice_public = alice.get_public_key_bytes()
bob_public = bob.get_public_key_bytes()

# Generate shared AES key
alice_key = alice.derive_session_key(bob_public)
bob_key = bob.derive_session_key(alice_public)

print("Keys Match:", alice_key == bob_key)

message = b"End-to-End Encrypted Voice"

nonce, cipher = alice.encrypt(message)

plain = bob.decrypt(nonce, cipher)

print("Original :", message)
print("Recovered:", plain)