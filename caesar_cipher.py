def encrypt(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():

            if ch.isupper():
                start = 65
            else:
                start = 97

            result += chr((ord(ch) - start + key) % 26 + start)

        else:
            result += ch

    return result


def decrypt(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():

            if ch.isupper():
                start = 65
            else:
                start = 97

            result += chr((ord(ch) - start - key) % 26 + start)

        else:
            result += ch

    return result


print("Caesar Cipher")
print("1. Encrypt")
print("2. Decrypt")

choice = int(input("Enter choice: "))

text = input("Enter text: ")
key = int(input("Enter key value: "))

if choice == 1:
    cipher = encrypt(text, key)
    print("Encrypted text:", cipher)

elif choice == 2:
    plain = decrypt(text, key)
    print("Decrypted text:", plain)

else:
    print("Invalid choice")