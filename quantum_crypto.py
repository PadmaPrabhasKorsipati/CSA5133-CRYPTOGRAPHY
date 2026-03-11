def pseudo_random(n, seed):

    result = []

    for i in range(n):
        seed = (seed * 7 + 3) % 10
        result.append(seed % 2)

    return result


def pseudo_bases(n, seed):

    bases = []

    for i in range(n):
        seed = (seed * 5 + 1) % 10

        if seed % 2 == 0:
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


print("Quantum Cryptography (BB84 Simulation)")

n = int(input("Enter number of bits: "))

alice_bits = pseudo_random(n, 5)
alice_bases = pseudo_bases(n, 7)

print("Alice Bits:", alice_bits)
print("Alice Bases:", alice_bases)


bob_bases = pseudo_bases(n, 9)

bob_results = measure(alice_bits, alice_bases, bob_bases)

print("Bob Bases:", bob_bases)
print("Bob Measurements:", bob_results)


shared_key = sift_key(alice_bits, alice_bases, bob_bases)

print("Shared Secret Key:", shared_key)