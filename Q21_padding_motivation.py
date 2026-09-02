def pkcs_style_padding(data, block_size):
    padding = block_size - (len(data) % block_size)
    if padding == 0:
        padding = block_size
    return data + bytes([padding] * padding)

def main():
    data = b"ABCDEFGH"
    padded = pkcs_style_padding(data, 8)
    print("Original:", data)
    print("Padded:", padded)
    print("Padding bytes added:", len(padded)-len(data))
    print("Motivation: the receiver can unambiguously determine whether padding exists.")

if __name__ == "__main__":
    main()

# Sample Output:
# Original: b'ABCDEFGH'
# Padded: b'ABCDEFGH\x08\x08\x08\x08\x08\x08\x08\x08'
# Padding bytes added: 8
# Motivation: the receiver can unambiguously determine whether padding exists.
