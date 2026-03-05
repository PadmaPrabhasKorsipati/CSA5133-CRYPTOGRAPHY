def encrypt(message, key):

    message = message.upper().replace(" ", "")

    if len(message) % 2 != 0:
        message += 'X'

    cipher = ""

    for i in range(0, len(message), 2):

        a = ord(message[i]) - 65
        b = ord(message[i+1]) - 65

        c1 = (key[0][0]*a + key[0][1]*b) % 26
        c2 = (key[1][0]*a + key[1][1]*b) % 26

        cipher += chr(c1 + 65)
        cipher += chr(c2 + 65)

    return cipher


def decrypt(cipher, inv_key):

    cipher = cipher.upper().replace(" ", "")
    message = ""

    for i in range(0, len(cipher), 2):

        a = ord(cipher[i]) - 65
        b = ord(cipher[i+1]) - 65

        p1 = (inv_key[0][0]*a + inv_key[0][1]*b) % 26
        p2 = (inv_key[1][0]*a + inv_key[1][1]*b) % 26

        message += chr(p1 + 65)
        message += chr(p2 + 65)

    # remove extra X if added
    if message[-1] == 'X':
        message = message[:-1]

    return message


print("Hill Cipher")
print("1. Encrypt")
print("2. Decrypt")

choice = int(input("Enter choice: "))


# Key matrix
key = [[3,3],
       [2,5]]

# Inverse key matrix
inv_key = [[15,17],
           [20,9]]

text = input("Enter message: ")


if choice == 1:

    cipher = encrypt(text, key)
    print("Encrypted message:", cipher)

elif choice == 2:

    plain = decrypt(text, inv_key)
    print("Decrypted message:", plain)

else:
    print("Invalid choice")