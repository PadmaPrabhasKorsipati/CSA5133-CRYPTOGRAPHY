# -------------------------
# SIMPLE DES FUNCTIONS
# -------------------------

def xor(a,b):
    result=""
    for i in range(len(a)):
        if a[i]==b[i]:
            result+="0"
        else:
            result+="1"
    return result


def des_encrypt(text,key):

    left = text[:32]
    right = text[32:]

    for i in range(16):

        temp = right

        right = xor(left,key[:32])

        left = temp

    return right + left


def des_decrypt(text,key):

    left = text[:32]
    right = text[32:]

    for i in range(16):

        temp = right

        right = xor(left,key[:32])

        left = temp

    return right + left


# -------------------------
# TRIPLE DES
# -------------------------

def triple_des_encrypt(plaintext, k1, k2, k3):

    step1 = des_encrypt(plaintext, k1)

    step2 = des_decrypt(step1, k2)

    cipher = des_encrypt(step2, k3)

    return cipher


def triple_des_decrypt(cipher, k1, k2, k3):

    step1 = des_decrypt(cipher, k3)

    step2 = des_encrypt(step1, k2)

    plaintext = des_decrypt(step2, k1)

    return plaintext


# -------------------------
# USER INTERFACE
# -------------------------

print("TRIPLE DES")
print("1. Encrypt")
print("2. Decrypt")

choice = int(input("Enter choice: "))

if choice == 1:

    plaintext = input("Enter 64-bit binary plaintext: ")

    k1 = input("Enter Key1 (48 bit): ")
    k2 = input("Enter Key2 (48 bit): ")
    k3 = input("Enter Key3 (48 bit): ")

    cipher = triple_des_encrypt(plaintext, k1, k2, k3)

    print("Cipher Text:", cipher)


elif choice == 2:

    cipher = input("Enter cipher text: ")

    k1 = input("Enter Key1 (48 bit): ")
    k2 = input("Enter Key2 (48 bit): ")
    k3 = input("Enter Key3 (48 bit): ")

    plaintext = triple_des_decrypt(cipher, k1, k2, k3)

    print("Decrypted Text:", plaintext)

else:

    print("Invalid Choice")