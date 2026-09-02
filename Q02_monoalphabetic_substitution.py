def encrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper()
    result = ""
    for ch in text:
        if ch.isalpha():
            result += key[alphabet.index(ch.upper())]
        else:
            result += ch
    return result

def main():
    text = input("Enter plaintext: ")
    key = input("Enter 26-letter substitution key: ")
    print("Ciphertext:", encrypt(text, key))

if __name__ == "__main__":
    main()

# Sample Output:
# Enter plaintext: HELLO
# Enter 26-letter substitution key: QWERTYUIOPASDFGHJKLZXCVBNM
# Ciphertext: ITSSG
