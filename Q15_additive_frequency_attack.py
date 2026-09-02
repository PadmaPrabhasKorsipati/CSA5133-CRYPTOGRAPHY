from collections import Counter

def decrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            result += chr((ord(ch.upper())-65-shift)%26+65)
        else:
            result += ch
    return result

def main():
    text = input("Enter additive cipher text: ")
    top = int(input("How many possible plaintexts? "))
    freq = Counter(c for c in text.upper() if c.isalpha())
    print("Cipher frequency:", freq.most_common())
    for shift in range(min(top,26)):
        print(f"{shift+1}. Shift {shift}: {decrypt(text,shift)}")

if __name__ == "__main__":
    main()

# Sample Output:
# Enter additive cipher text: KHOOR ZRUOG
# How many possible plaintexts? 5
# Cipher frequency: [('O', 2), ('R', 2), ...]
# 1. Shift 0: KHOOR ZRUOG
# 2. Shift 1: JGNNQ YQTF...
# ...
