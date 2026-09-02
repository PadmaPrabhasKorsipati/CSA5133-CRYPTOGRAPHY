import secrets

def main():
    message = "HELLO"
    print("Message:", message)
    print("Signature 1 uses random k:", secrets.randbelow(1000)+1)
    print("Signature 2 uses a different random k:", secrets.randbelow(1000)+1)
    print("Implication: DSA signatures can differ for the same message.")
    print("RSA signatures using deterministic signing with the same key and message can be identical.")

if __name__ == "__main__":
    main()

# Sample Output:
# Message: HELLO
# Signature 1 uses random k: 417
# Signature 2 uses a different random k: 829
# Implication: DSA signatures can differ for the same message.
# RSA signatures using deterministic signing with the same key and message can be identical.
