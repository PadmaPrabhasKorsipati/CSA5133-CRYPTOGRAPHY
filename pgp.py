import hashlib

# XOR encryption and decryption function
def encrypt_decrypt(data, key):
    result = ""
    for i in range(len(data)):
        result += chr(ord(data[i]) ^ ord(key[i % len(key)]))
    return result


# Digital signature using SHA-256
def generate_signature(message):
    return hashlib.sha256(message.encode()).hexdigest()


print("PGP Algorithm")
print("1. Encrypt")
print("2. Decrypt")

choice = int(input("Enter choice: "))


# ENCRYPT
if choice == 1:

    message = input("Enter message: ")
    key = input("Enter secret key: ")

    signature = generate_signature(message)

    combined = message + "|" + signature

    encrypted_message = encrypt_decrypt(combined, key)

    print("\nEncrypted Message:", encrypted_message)


# DECRYPT
elif choice == 2:

    encrypted_message = input("Enter encrypted message: ")
    key = input("Enter secret key: ")

    decrypted = encrypt_decrypt(encrypted_message, key)

    message, received_signature = decrypted.split("|")

    new_signature = generate_signature(message)

    print("\nDecrypted Message:", message)

    if new_signature == received_signature:
        print("Signature Verified")
    else:
        print("Signature Verification Failed")


else:
    print("Invalid choice")