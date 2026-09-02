def main():
    print("DES subkey structure:")
    print("C_i contains 28 bits from one subset of the key.")
    print("D_i contains 28 bits from the disjoint subset.")
    print("Each round subkey is formed from selected bits of C_i and D_i.")
    print("Subkey size = 48 bits = 24 bits from C_i + 24 bits from D_i.")

if __name__ == "__main__":
    main()

# Sample Output:
# DES subkey structure:
# C_i contains 28 bits from one subset of the key.
# D_i contains 28 bits from the disjoint subset.
# Each round subkey is formed from selected bits of C_i and D_i.
# Subkey size = 48 bits = 24 bits from C_i + 24 bits from D_i.
