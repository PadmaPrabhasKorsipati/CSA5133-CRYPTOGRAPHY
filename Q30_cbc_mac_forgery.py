def xor_bits(a,b):
    return bytes(x^y for x,y in zip(a,b))

def main():
    X = b"BLOCK123"
    T = b"MACVALUE"
    forged_second = xor_bits(X,T)
    print("X:", X)
    print("T = MAC(K,X):", T)
    print("X XOR T:", forged_second)
    print("Forged message structure: X || (X XOR T)")
    print("The CBC-MAC construction can allow this extension forgery for variable-length messages.")

if __name__ == "__main__":
    main()

# Sample Output:
# X: b'BLOCK123'
# T = MAC(K,X): b'MACVALUE'
# X XOR T: b'\x0f\x0c\x0c\x0f\x1d\x13\x15\x16'
# Forged message structure: X || (X XOR T)
# The CBC-MAC construction can allow this extension forgery for variable-length messages.
