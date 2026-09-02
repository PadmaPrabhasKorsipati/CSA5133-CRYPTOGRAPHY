def pad(data, block_size):
    count = block_size - len(data) % block_size
    if count == 0:
        count = block_size
    return data + bytes([count])*count

def main():
    data = b"ABCDEFGH"
    result = pad(data, 8)
    print("Original:", data)
    print("Padded:", result)
    print("Reason for padding a complete final block: unambiguous padding removal.")

if __name__ == "__main__":
    main()

# Sample Output:
# Original: b'ABCDEFGH'
# Padded: b'ABCDEFGH\x08\x08\x08\x08\x08\x08\x08\x08'
# Reason for padding a complete final block: unambiguous padding removal.
