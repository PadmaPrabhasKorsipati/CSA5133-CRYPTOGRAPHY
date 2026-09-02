def caesar_encrypt(text, k):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result += chr((ord(ch) - base + k) % 26 + base)
        else:
            result += ch
    return result

def main():
    text = input("Enter plaintext: ")
    k = int(input("Enter shift (1-25): "))
    print("Ciphertext:", caesar_encrypt(text, k))

if __name__ == "__main__":
    main()

# Sample Output:
# Enter plaintext: HELLO WORLD
# Enter shift (1-25): 3
# Ciphertext: KHOOR ZRUOG
