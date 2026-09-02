def determinant(m):
    return m[0][0]*m[1][1]-m[0][1]*m[1][0]

def main():
    print("Hill cipher known-plaintext attack demonstration")
    print("Collect enough plaintext-ciphertext pairs to form invertible plaintext matrices.")
    print("For a 2x2 Hill cipher, if P is invertible modulo 26 and C = KP, then K = C(P^-1) mod 26.")
    print("A chosen-plaintext attack can select plaintext blocks that make P easy to invert.")

if __name__ == "__main__":
    main()

# Sample Output:
# Hill cipher known-plaintext attack demonstration
# K = C(P^-1) mod 26
# A chosen-plaintext attack can select plaintext blocks that make P easy to invert.
