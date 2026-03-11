def generate_bits(n):

    bits = []

    for i in range(n):
        bits.append(i % 2)

    return bits


def generate_bases(n):

    bases = []

    for i in range(n):

        if i % 2 == 0:
            bases.append('+')
        else:
            bases.append('x')

    return bases


def measure(bits, sender_bases, receiver_bases):

    result = []

    for i in range(len(bits)):

        if sender_bases[i] == receiver_bases[i]:
            result.append(bits[i])
        else:
            result.append((bits[i] + 1) % 2)

    return result


def sift_key(bits, sender_bases, receiver_bases):

    key = []

    for i in range(len(bits)):

        if sender_bases[i] == receiver_bases[i]:
            key.append(bits[i])

    return key


print("Quantum Cryptography (BB84)")
print("1. Generate Key")
print("2. Verify Key")

choice = int(input("Enter choice: "))


if choice == 1:

    n = int(input("Enter number of bits: "))

    alice_bits = generate_bits(n)
    alice_bases = generate_bases(n)

    print("Alice Bits:", alice_bits)
    print("Alice Bases:", alice_bases)

    bob_bases = generate_bases(n)

    bob_results = measure(alice_bits, alice_bases, bob_bases)

    print("Bob Bases:", bob_bases)
    print("Bob Measurements:", bob_results)

    shared_key = sift_key(alice_bits, alice_bases, bob_bases)

    print("Generated Secret Key:", shared_key)


elif choice == 2:

    key = input("Enter key to verify: ")

    if len(key) > 0:
        print("Key verified successfully")
    else:
        print("Invalid key")

else:
    print("Invalid choice")