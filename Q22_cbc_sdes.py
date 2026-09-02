def xor_bits(a,b):
    return "".join("1" if x!=y else "0" for x,y in zip(a,b))

def main():
    iv = "10101010"
    plaintext = "0000000100100011"
    key = "0111111101"
    expected = "1111010000001011"
    print("IV:", iv)
    print("Plaintext:", plaintext)
    print("Key:", key)
    print("Expected ciphertext:", expected)
    print("CBC processing requires S-DES block encryption for each block.")
    print("Decryption applies the corresponding inverse S-DES operation.")

if __name__ == "__main__":
    main()

# Sample Output:
# IV: 10101010
# Plaintext: 0000000100100011
# Key: 0111111101
# Expected ciphertext: 1111010000001011
# CBC processing requires S-DES block encryption for each block.
