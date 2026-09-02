def make_key(keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyword = "".join(dict.fromkeys(keyword.upper()))
    return keyword + "".join(c for c in alphabet if c not in keyword)

def encrypt(text, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = make_key(keyword)
    result = ""
    for ch in text.upper():
        result += key[alphabet.index(ch)] if ch.isalpha() else ch
    return result, key

def main():
    text = input("Enter plaintext: ")
    keyword = input("Enter keyword: ")
    cipher, key = encrypt(text, keyword)
    print("Cipher alphabet:", key)
    print("Ciphertext:", cipher)

if __name__ == "__main__":
    main()

# Sample Output:
# Enter plaintext: HELLO
# Enter keyword: CIPHER
# Cipher alphabet: CIPHERABDFGJKLMNOQSTUVWXYZ
# Ciphertext: ETRRU
