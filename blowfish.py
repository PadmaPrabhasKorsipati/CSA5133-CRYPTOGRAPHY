def xor(a,b):
    result=""
    for i in range(len(a)):
        if a[i]==b[i]:
            result+="0"
        else:
            result+="1"
    return result


def F(x):

    # simple substitution function
    return x[::-1]


def encrypt(text,key):

    left=text[:4]
    right=text[4:]

    for i in range(4):  # simplified rounds

        left=xor(left,key[:4])

        f=F(left)

        right=xor(right,f)

        left,right=right,left

    left,right=right,left

    return left+right


def decrypt(cipher,key):

    left=cipher[:4]
    right=cipher[4:]

    for i in range(4):

        left=xor(left,key[:4])

        f=F(left)

        right=xor(right,f)

        left,right=right,left

    left,right=right,left

    return left+right


print("Blowfish Algorithm")
print("1. Encrypt")
print("2. Decrypt")

choice=input("Enter choice: ")

text=input("Enter 8-bit binary text: ")
key=input("Enter binary key: ")

if choice=="1":

    cipher=encrypt(text,key)
    print("Encrypted:",cipher)

elif choice=="2":

    plain=decrypt(text,key)
    print("Decrypted:",plain)

else:
    print("Invalid choice")



#hi
