def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def affine_encrypt(text, a, b):
    result = ""
    for ch in text:
        if ch.isalpha():
            p = ord(ch.upper()) - ord("A")
            c = (a*p+b) % 26
            result += chr(c+ord("A"))
        else:
            result += ch
    return result

def main():
    print("b can be any integer modulo 26.")
    print("Allowed a values must be relatively prime to 26.")
    print("Allowed a values: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25")
    text = input("Enter plaintext: ")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    if gcd(a, 26) != 1:
        print("Invalid a. Encryption is not one-to-one.")
        return
    print("Ciphertext:", affine_encrypt(text, a, b))

if __name__ == "__main__":
    main()

# Sample Output:
# b can be any integer modulo 26.
# Allowed a values must be relatively prime to 26.
# Enter plaintext: HELLO
# Enter a: 5
# Enter b: 8
# Ciphertext: RCLLA
