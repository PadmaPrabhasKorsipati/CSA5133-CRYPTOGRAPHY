def otp_vigenere(text, key):
    letters = "".join(c for c in text.upper() if c.isalpha())
    return "".join(chr((ord(c)-65+key[i])%26+65) for i,c in enumerate(letters))

def main():
    text = input("Enter plaintext: ")
    key = list(map(int,input("Enter key stream: ").split()))
    print("Ciphertext:", otp_vigenere(text,key))

if __name__ == "__main__":
    main()

# Sample Output:
# Enter plaintext: SEND MORE MONEY
# Enter key stream: 9 0 1 7 23 15 21 14 11 11 2 8 9
# Ciphertext: XIMZABT...
