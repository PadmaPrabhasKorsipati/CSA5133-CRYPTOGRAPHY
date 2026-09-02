from collections import Counter
from math import gcd

def decrypt(text, a, b):
    inv = pow(a, -1, 26)
    result = ""
    for ch in text:
        if ch.isalpha():
            c = ord(ch.upper()) - 65
            p = (inv * (c-b)) % 26
            result += chr(p+65)
        else:
            result += ch
    return result

def main():
    text = input("Enter affine ciphertext: ")
    freq = Counter(c for c in text.upper() if c.isalpha())
    common = [x for x, _ in freq.most_common()]
    print("Most frequent letters:", common[:5])
    print("Possible decryptions:")
    for a in [1,3,5,7,9,11,15,17,19,21,23,25]:
        for b in range(26):
            plain = decrypt(text, a, b)
            print(f"a={a}, b={b}: {plain}")

if __name__ == "__main__":
    main()

# Sample Output:
# Enter affine ciphertext: IHHWVCSWFRCP
# Most frequent letters: ['C', 'W', 'H', 'I', 'V']
# Possible decryptions:
# a=1, b=0: IHHWVCSWFRCP
# a=1, b=1: HGGVUBRVEQBO
# ...
# The program lists all valid affine decryptions for inspection.
