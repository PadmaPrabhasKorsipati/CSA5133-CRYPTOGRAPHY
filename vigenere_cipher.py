def encrypt(text, key):
    result = ""
    j = 0

    for ch in text:
        if ch.isalpha():

            if ch.isupper():
                start = 65
            else:
                start = 97

            shift = ord(key[j % len(key)].upper()) - 65

            result += chr((ord(ch) - start + shift) % 26 + start)
            j += 1

        else:
            result += ch

    return result


def decrypt(text, key):
    result = ""
    j = 0

    for ch in text:
        if ch.isalpha():

            if ch.isupper():
                start = 65
            else:
                start = 97

            shift = ord(key[j % len(key)].upper()) - 65

            result += chr((ord(ch) - start - shift) % 26 + start)
            j += 1

        else:
            result += ch

    return result


print("Vigenere Cipher")
print("1. Encrypt")
print("2. Decrypt")

choice = int(input("Enter choice: "))

text = input("Enter text: ")
key = input("Enter key: ")

if choice == 1:
    cipher = encrypt(text, key)
    print("Encrypted text:", cipher)

elif choice == 2:
    plain = decrypt(text, key)
    print("Decrypted text:", plain)

else:
    print("Invalid choice")