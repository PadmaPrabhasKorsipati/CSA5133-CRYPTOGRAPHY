def encrypt(text, key):
    result = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for ch in text.upper():
        if ch.isalpha():
            index = alphabet.index(ch)
            result += key[index]
        else:
            result += ch

    return result


def decrypt(cipher, key):
    result = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for ch in cipher:
        if ch.isalpha():
            index = key.index(ch)
            result += alphabet[index]
        else:
            result += ch

    return result


print("Monoalphabetic Cipher")
print("1. Encrypt")
print("2. Decrypt")

choice = int(input("Enter choice: "))

text = input("Enter text: ").upper()

# substitution key
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

if choice == 1:
    cipher = encrypt(text, key)
    print("Encrypted text:", cipher)

elif choice == 2:
    plain = decrypt(text, key)
    print("Decrypted text:", plain)

else:
    print("Invalid choice")