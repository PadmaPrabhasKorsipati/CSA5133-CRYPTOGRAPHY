def encrypt(text, rails):

    text = text.replace(" ", "")
    fence = ['' for _ in range(rails)]

    rail = 0
    direction = 1

    for ch in text:

        fence[rail] += ch
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    cipher = ""

    for r in fence:
        cipher += r

    return cipher


def decrypt(cipher, rails):

    n = len(cipher)
    fence = [['' for _ in range(n)] for _ in range(rails)]

    rail = 0
    direction = 1

    for i in range(n):

        fence[rail][i] = '*'
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    index = 0

    for i in range(rails):
        for j in range(n):
            if fence[i][j] == '*' and index < n:
                fence[i][j] = cipher[index]
                index += 1

    result = ""
    rail = 0
    direction = 1

    for i in range(n):

        result += fence[rail][i]
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    return result


print("Rail Fence Cipher")
print("1. Encrypt")
print("2. Decrypt")

choice = int(input("Enter choice: "))

text = input("Enter message: ")
rails = int(input("Enter number of rails: "))

if choice == 1:

    cipher = encrypt(text, rails)
    print("Encrypted message:", cipher)

elif choice == 2:

    plain = decrypt(text, rails)
    print("Decrypted message:", plain)

else:
    print("Invalid choice")