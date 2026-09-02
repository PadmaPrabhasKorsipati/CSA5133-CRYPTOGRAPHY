from collections import Counter

def decrypt(text, shift):
    return "".join(chr((ord(c.upper())-65-shift)%26+65) if c.isalpha() else c for c in text)

def main():
    text=input("Enter additive ciphertext: ")
    top=int(input("Enter top candidates: "))
    freq=Counter(c for c in text.upper() if c.isalpha())
    print("Frequency:",freq.most_common())
    for shift in range(min(26,top)):
        print(f"Candidate {shift+1}: {decrypt(text,shift)}")

if __name__ == "__main__":
    main()

# Sample Output:
# Enter additive ciphertext: KHOOR ZRUOG
# Enter top candidates: 10
# Frequency: [('O', 2), ('R', 2), ('K', 1), ('H', 1), ('Z', 1), ('U', 1), ('G', 1)]
# Candidate 1: KHOOR ZRUOG
# Candidate 2: JGNNQ YQTF...
# ...
