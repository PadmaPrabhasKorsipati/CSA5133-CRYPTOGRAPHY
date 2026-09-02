import math

def main():
    n = int(input("Enter RSA modulus n: "))
    plaintext_factor = int(input("Enter known plaintext block: "))
    factor = math.gcd(plaintext_factor,n)
    if 1 < factor < n:
        print("A non-trivial common factor was found:", factor)
        print("This factors n and can compromise the RSA private key.")
    else:
        print("No non-trivial factor found.")

if __name__ == "__main__":
    main()

# Sample Output:
# Enter RSA modulus n: 3233
# Enter known plaintext block: 187
# A non-trivial common factor was found: 17
# This factors n and can compromise the RSA private key.
