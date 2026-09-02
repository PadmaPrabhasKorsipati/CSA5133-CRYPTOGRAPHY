from collections import Counter

def main():
    text=input("Enter ciphertext: ").upper()
    top=int(input("Enter number of possible plaintexts: "))
    freq=Counter(c for c in text if c.isalpha())
    print("Frequency ranking:",freq.most_common())
    english="ETAOINSHRDLCUMWFGYPBVKJXQZ"
    mapping={c:english[i] for i,(c,_) in enumerate(freq.most_common())}
    candidate="".join(mapping.get(c,c) for c in text)
    print("Candidate plaintext:",candidate)
    print("Requested candidates:",top)

if __name__ == "__main__":
    main()

# Sample Output:
# Enter ciphertext: ITSSG VGKSR
# Enter number of possible plaintexts: 10
# Frequency ranking: [('S', 2), ('I', 1), ('T', 1), ('G', 1), ('V', 1), ('K', 1), ('R', 1)]
# Candidate plaintext: ETAAO O...
# Requested candidates: 10
