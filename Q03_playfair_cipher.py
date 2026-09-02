def create_matrix(key):
    key = "".join(dict.fromkeys(key.upper().replace("J", "I")))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    chars = key + "".join(c for c in alphabet if c not in key)
    return [chars[i:i+5] for i in range(0, 25, 5)]

def prepare(text):
    text = "".join(c for c in text.upper() if c.isalpha()).replace("J", "I")
    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "X"
        if a == b:
            result += a + "X"
            i += 1
        else:
            result += a + b
            i += 2
    if len(result) % 2:
        result += "X"
    return result

def position(matrix, ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c

def encrypt(text, key):
    matrix = create_matrix(key)
    text = prepare(text)
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = position(matrix, a)
        r2, c2 = position(matrix, b)
        if r1 == r2:
            result += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:
            result += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]
    return result, matrix

def main():
    key = input("Enter keyword: ")
    text = input("Enter plaintext: ")
    cipher, matrix = encrypt(text, key)
    print("Playfair Matrix:")
    for row in matrix:
        print(" ".join(row))
    print("Ciphertext:", cipher)

if __name__ == "__main__":
    main()

# Sample Output:
# Enter keyword: MONARCHY
# Enter plaintext: INSTRUMENTS
# Playfair Matrix:
# M O N A R
# C H Y B D
# E F G I K
# L P Q S T
# U V W X Z
# Ciphertext: GATLMZCLRQXA
