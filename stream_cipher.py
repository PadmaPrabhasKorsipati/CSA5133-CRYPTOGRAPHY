def xor_operation(a, b):
    result = ""

    for i in range(len(a)):

        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"

    return result


def encrypt(plaintext, key):

    cipher = xor_operation(plaintext, key)
    return cipher


def decrypt(ciphertext, key):

    plain = xor_operation(ciphertext, key)
    return plain


print("Stream Cipher")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter choice: ")

text = input("Enter binary text: ")
key = input("Enter binary key: ")

if len(text) != len(key):
    print("Text and key must be same length")

else:

    if choice == "1":

        cipher = encrypt(text, key)
        print("Encrypted:", cipher)

    elif choice == "2":

        plain = decrypt(text, key)
        print("Decrypted:", plain)

    else:
        print("Invalid choice")