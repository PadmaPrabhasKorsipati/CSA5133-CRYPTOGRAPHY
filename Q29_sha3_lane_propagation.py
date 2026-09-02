def main():
    block_size = 1024
    rate_lanes = block_size // 64
    total_lanes = 25
    capacity_lanes = total_lanes - rate_lanes
    print("Block size:", block_size, "bits")
    print("Rate lanes:", rate_lanes)
    print("Total lanes:", total_lanes)
    print("Capacity lanes:", capacity_lanes)
    print("Without permutation, zero capacity lanes remain zero.")
    print("Therefore, the capacity lanes never obtain a nonzero bit under the stated assumption.")

if __name__ == "__main__":
    main()

# Sample Output:
# Block size: 1024 bits
# Rate lanes: 16
# Total lanes: 25
# Capacity lanes: 9
# Without permutation, zero capacity lanes remain zero.
# Therefore, the capacity lanes never obtain a nonzero bit under the stated assumption.
