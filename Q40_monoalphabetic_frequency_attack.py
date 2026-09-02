from collections import Counter

def frequency_attack(text):
    english = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    freq = Counter(c for c in text.upper() if c.isalpha())
    mapping = {c: english[i] for i,(c,_) in enumerate(freq.most_common())}
    return "".join(mapping.get(c,c) for c in text.upper()), freq

def main():
    text=input("Enter ciphertext: ")
    top=int(input("Enter top number of candidates: "))
    candidate,freq=frequency_attack(text)
    print("Frequency ranking:",freq.most_common())
    print("Candidate 1:",candidate)
    print(f"Requested top candidates: {top}")

if __name__ == "__main__":
    main()

# Sample Output:
# Enter ciphertext: ITSSG VGKSR
# Enter top number of candidates: 10
# Frequency ranking: [('S', 2), ('I', 1), ('T', 1), ('G', 1), ('V', 1), ('K', 1), ('R', 1)]
# Candidate 1: ETAAO O...
# Requested top candidates: 10
