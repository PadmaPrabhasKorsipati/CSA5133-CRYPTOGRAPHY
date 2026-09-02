def main():
    counter = "00000000"
    plaintext = "000000010000001000000100"
    key = "0111111101"
    expected = "001110000100111100110010"
    print("Initial counter:", counter)
    print("Plaintext:", plaintext)
    print("Key:", key)
    print("Expected ciphertext:", expected)
    print("CTR encrypts each counter value and XORs the keystream with plaintext.")
    print("Decryption uses the same operation.")

if __name__ == "__main__":
    main()

# Sample Output:
# Initial counter: 00000000
# Plaintext: 000000010000001000000100
# Key: 0111111101
# Expected ciphertext: 001110000100111100110010
# Decryption uses the same operation.
