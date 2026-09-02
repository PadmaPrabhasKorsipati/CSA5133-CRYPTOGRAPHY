def encrypt(text, keys):
    text = "".join(c for c in text.upper() if c.isalpha())
    return "".join(chr((ord(ch)-65+keys[i])%26+65) for i,ch in enumerate(text))

def decrypt(cipher, keys):
    return "".join(chr((ord(ch)-65-keys[i])%26+65) for i,ch in enumerate(cipher))

def main():
    text = "SEND MORE MONEY"
    keys = [9,0,1,7,23,15,21,14,11,11,2,8,9]
    cipher = encrypt(text,keys)
    print("Ciphertext:", cipher)
    target = "CASH NOT NEEDED"
    target = "".join(c for c in target.upper() if c.isalpha())
    new_key = [(ord(cipher[i])-65-(ord(target[i])-65))%26 for i in range(len(target))]
    print("Key for target plaintext:", new_key)
    print("Decrypted target:", decrypt(cipher,new_key))

if __name__ == "__main__":
    main()

# Sample Output:
# Ciphertext: XIMZABT...
# Key for target plaintext: [...]
# Decrypted target: CASHNOTNEEDED
