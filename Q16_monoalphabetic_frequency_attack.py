from collections import Counter

def main():
    text = input("Enter substitution ciphertext: ")
    top = int(input("Enter number of possible plaintexts: "))
    frequency = Counter(c for c in text.upper() if c.isalpha())
    print("Letter frequency:")
    for letter,count in frequency.most_common():
        print(letter, count)
    print()
    print(f"Generating up to {top} candidate mappings using frequency ordering.")
    english = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    cipher_letters = [x for x,_ in frequency.most_common()]
    mapping = dict(zip(cipher_letters, english))
    result = "".join(mapping.get(c,c) for c in text.upper())
    print("Candidate plaintext:", result)

if __name__ == "__main__":
    main()

# Sample Output:
# Enter substitution ciphertext: ITSSG VGKSR
# Enter number of possible plaintexts: 10
# Letter frequency:
# S 2
# ...
# Candidate plaintext: ...
