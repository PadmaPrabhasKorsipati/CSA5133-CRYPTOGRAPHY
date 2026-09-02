def main():
    print("Encrypting each alphabetic character separately with deterministic RSA is not secure.")
    print("There are only 26 possible plaintext values.")
    print("An attacker can encrypt all 26 possibilities using the public key and build a lookup table.")
    print("This is the most efficient attack for the described scheme.")

if __name__ == "__main__":
    main()

# Sample Output:
# Encrypting each alphabetic character separately with deterministic RSA is not secure.
# There are only 26 possible plaintext values.
# An attacker can encrypt all 26 possibilities using the public key and build a lookup table.
# This is the most efficient attack for the described scheme.
