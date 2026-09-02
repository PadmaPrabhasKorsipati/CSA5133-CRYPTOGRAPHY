def matrix_from_key(key):
    key = "".join(dict.fromkeys(key.upper().replace("J","I")))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    s = key + "".join(c for c in alphabet if c not in key)
    return [s[i:i+5] for i in range(0,25,5)]

def pos(m, ch):
    for r in range(5):
        for c in range(5):
            if m[r][c] == ch:
                return r,c

def decrypt(cipher, key):
    m = matrix_from_key(key)
    result = ""
    for i in range(0,len(cipher),2):
        a,b = cipher[i],cipher[i+1]
        r1,c1 = pos(m,a); r2,c2 = pos(m,b)
        if r1 == r2:
            result += m[r1][(c1-1)%5] + m[r2][(c2-1)%5]
        elif c1 == c2:
            result += m[(r1-1)%5][c1] + m[(r2-1)%5][c2]
        else:
            result += m[r1][c2] + m[r2][c1]
    return result

def main():
    key = input("Enter keyword: ")
    cipher = input("Enter Playfair ciphertext: ").replace(" ","").upper()
    print("Plaintext:", decrypt(cipher,key))

if __name__ == "__main__":
    main()

# Sample Output:
# Enter keyword: MONARCHY
# Enter Playfair ciphertext: GATLMZCLRQXA
# Plaintext: INSTRUMENTSX
