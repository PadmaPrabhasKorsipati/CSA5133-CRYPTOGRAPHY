def left_rotate(x, n):
    n = n % 32
    return ((x << n) & 0xFFFFFFFF) | (x >> (32 - n))


def right_rotate(x, n):
    n = n % 32
    return (x >> n) | ((x << (32 - n)) & 0xFFFFFFFF)


def encrypt(A, B, key, rounds):

    for i in range(rounds):

        A = (A ^ B)
        A = left_rotate(A, B % 32)
        A = (A + key) % (2**32)

        B = (B ^ A)
        B = left_rotate(B, A % 32)
        B = (B + key) % (2**32)

    return A, B


def decrypt(A, B, key, rounds):

    for i in range(rounds):

        B = (B - key) % (2**32)
        B = right_rotate(B, A % 32)
        B = B ^ A

        A = (A - key) % (2**32)
        A = right_rotate(A, B % 32)
        A = A ^ B

    return A, B


print("RC5 Algorithm")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter choice: ")

A = int(input("Enter first half: "))
B = int(input("Enter second half: "))

key = int(input("Enter key: "))
rounds = int(input("Enter rounds: "))


if choice == "1":

    A, B = encrypt(A, B, key, rounds)
    print("Encrypted:", A, B)

elif choice == "2":

    A, B = decrypt(A, B, key, rounds)
    print("Decrypted:", A, B)

else:
    print("Invalid choice")