def reverse_keys(keys):
    return list(reversed(keys))

def main():
    keys = [f"K{i}" for i in range(1,17)]
    print("Encryption key order:", keys)
    print("Decryption key order:", reverse_keys(keys))

if __name__ == "__main__":
    main()

# Sample Output:
# Encryption key order: ['K1', 'K2', 'K3', ..., 'K16']
# Decryption key order: ['K16', 'K15', 'K14', ..., 'K1']
