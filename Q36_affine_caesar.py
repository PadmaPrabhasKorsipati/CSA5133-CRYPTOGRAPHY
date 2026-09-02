def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    if gcd(a,26) != 1:
        print("Invalid a. gcd(a,26) must be 1.")
        return
    text = input("Enter plaintext: ")
    result = ""
    for ch in text.upper():
        if ch.isalpha():
            p=ord(ch)-65
            result += chr((a*p+b)%26+65)
        else:
            result += ch
    print("Ciphertext:",result)

if __name__ == "__main__":
    main()

# Sample Output:
# Enter a: 5
# Enter b: 8
# Enter plaintext: HELLO
# Ciphertext: RCLLA
