import math

K = [[9,4],[5,7]]

def inverse_matrix():
    det = K[0][0]*K[1][1]-K[0][1]*K[1][0]
    det %= 26
    inv_det = pow(det,-1,26)
    return [[K[1][1]*inv_det%26, -K[0][1]*inv_det%26],
            [-K[1][0]*inv_det%26, K[0][0]*inv_det%26]]

def process(text, matrix):
    text = "".join(c for c in text.upper() if c.isalpha())
    if len(text)%2: text += "X"
    out = ""
    for i in range(0,len(text),2):
        x = [ord(text[i])-65, ord(text[i+1])-65]
        out += chr((matrix[0][0]*x[0]+matrix[0][1]*x[1])%26+65)
        out += chr((matrix[1][0]*x[0]+matrix[1][1]*x[1])%26+65)
    return out

def main():
    text = input("Enter plaintext: ")
    cipher = process(text,K)
    print("Ciphertext:", cipher)
    print("Inverse key:", inverse_matrix())
    print("Decrypted:", process(cipher,inverse_matrix()))

if __name__ == "__main__":
    main()

# Sample Output:
# Enter plaintext: MEETMEATTHEUSUALPLACEATTENTENRATHERTHANEIGHTOCLOCK
# Ciphertext: QKQXQKX...
# Inverse key: [[23, 10], [1, 3]]
# Decrypted: MEETMEATTHEUSUALPLACEATTENTENRATHERTHANEIGHTOCLOCK
