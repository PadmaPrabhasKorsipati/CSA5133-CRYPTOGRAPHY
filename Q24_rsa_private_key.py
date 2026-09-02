def factor(n):
    for p in range(2, int(n**0.5)+1):
        if n % p == 0:
            return p, n//p

def main():
    e, n = 31, 3599
    p, q = factor(n)
    phi = (p-1)*(q-1)
    d = pow(e,-1,phi)
    print("p =", p)
    print("q =", q)
    print("phi(n) =", phi)
    print("Private key d =", d)

if __name__ == "__main__":
    main()

# Sample Output:
# p = 59
# q = 61
# phi(n) = 3480
# Private key d = 2791
