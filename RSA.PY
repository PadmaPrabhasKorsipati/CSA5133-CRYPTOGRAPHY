def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None


def power(base, exp, mod):
    result = 1
    for i in range(exp):
        result = (result * base) % mod
    return result


def encrypt(msg, e, n):
    return power(msg, e, n)


def decrypt(cipher, d, n):
    return power(cipher, d, n)


print("RSA Algorithm")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter choice: ")

p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))

n = p * q
phi = (p - 1) * (q - 1)

print("n =", n)
print("phi =", phi)

e = int(input("Enter public key e: "))

if gcd(e, phi) != 1:
    print("Invalid public key")
else:

    d = mod_inverse(e, phi)

    print("Private key d =", d)

    if choice == "1":

        msg = int(input("Enter message: "))
        cipher = encrypt(msg, e, n)
        print("Encrypted message =", cipher)

    elif choice == "2":

        cipher = int(input("Enter cipher: "))
        plain = decrypt(cipher, d, n)
        print("Decrypted message =", plain)

    else:
        print("Invalid choice")