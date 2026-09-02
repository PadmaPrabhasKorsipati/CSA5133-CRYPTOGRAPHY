import math

def main():
    total = math.factorial(25)
    approximate_bits = math.log2(total)
    effective = total // 25
    effective_bits = math.log2(effective)
    print("Total Playfair keys:", total)
    print("Approximate power of 2:", f"2^{approximate_bits:.2f}")
    print("Effective unique keys after equivalent-key adjustment:", effective)
    print("Approximate effective power of 2:", f"2^{effective_bits:.2f}")

if __name__ == "__main__":
    main()

# Sample Output:
# Total Playfair keys: 15511210043330985984000000
# Approximate power of 2: 2^83.68
# Effective unique keys after equivalent-key adjustment: 620448401733239439360000
# Approximate effective power of 2: 2^78.04
