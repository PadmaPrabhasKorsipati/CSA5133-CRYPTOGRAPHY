
def power(a, b, p):
    result = 1
    for i in range(b):
        result = (result * a) % p
    return result


def diffie_hellman():
    p = int(input("Enter prime number (p): "))
    g = int(input("Enter primitive root (g): "))

    # private keys
    a = int(input("Enter private key of User A: "))
    b = int(input("Enter private key of User B: "))

    # public keys
    A = power(g, a, p)
    B = power(g, b, p)

    print("Public key of A:", A)
    print("Public key of B:", B)

    # shared secret
    keyA = power(B, a, p)
    keyB = power(A, b, p)

    print("Secret key for A:", keyA)
    print("Secret key for B:", keyB)


diffie_hellman()
