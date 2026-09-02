def left_shift_1(value, bits):
    mask = (1 << bits) - 1
    return (value << 1) & mask

def main():
    print("For 64-bit CMAC, the reduction constant Rb is 0x1B.")
    print("For 128-bit CMAC, the reduction constant Rb is 0x87.")
    print("The first subkey is obtained by left shifting L and conditionally XORing Rb.")
    print("The second subkey is obtained by applying the same operation to the first subkey.")
    print("The shift moves each bit toward the next polynomial degree; XOR performs reduction when needed.")

if __name__ == "__main__":
    main()

# Sample Output:
# For 64-bit CMAC, the reduction constant Rb is 0x1B.
# For 128-bit CMAC, the reduction constant Rb is 0x87.
# The first subkey is obtained by left shifting L and conditionally XORing Rb.
# The second subkey is obtained by applying the same operation to the first subkey.
