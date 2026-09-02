def main():
    print("ECB/CBC error propagation analysis")
    print("a. In CBC, an error in C1 corrupts P1 and causes a corresponding bit error in P2.")
    print("   Blocks beyond P2 are not affected.")
    print("b. A bit error in source P1 changes C1 and propagates through subsequent ciphertext blocks.")
    print("   With standard CBC chaining, later plaintext recovery is restored after the affected block.")

if __name__ == "__main__":
    main()

# Sample Output:
# ECB/CBC error propagation analysis
# a. In CBC, an error in C1 corrupts P1 and causes a corresponding bit error in P2.
#    Blocks beyond P2 are not affected.
# b. A bit error in source P1 propagates through the ciphertext chain.
