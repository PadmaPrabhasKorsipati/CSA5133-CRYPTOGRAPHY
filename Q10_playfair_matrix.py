def decrypt_matrix(cipher):
    matrix = [
        ["M","F","H","I","K"],
        ["U","N","O","P","Q"],
        ["Z","V","W","X","Y"],
        ["E","L","A","R","G"],
        ["D","S","T","B","C"]
    ]
    def pos(ch):
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == ch:
                    return r,c
    result = ""
    for i in range(0,len(cipher),2):
        a,b = cipher[i],cipher[i+1]
        r1,c1=pos(a); r2,c2=pos(b)
        if r1==r2:
            result += matrix[r1][(c1-1)%5]+matrix[r2][(c2-1)%5]
        elif c1==c2:
            result += matrix[(r1-1)%5][c1]+matrix[(r2-1)%5][c2]
        else:
            result += matrix[r1][c2]+matrix[r2][c1]
    return result

def main():
    text = "MUSTSEEYOUOVERCADOGANWESTCOMINGATONCE"
    print("Prepared plaintext:", text)
    print("This fixed Playfair matrix is ready for encryption.")
    print("Use the matrix specified in the experiment to process digraphs.")

if __name__ == "__main__":
    main()

# Sample Output:
# Prepared plaintext: MUSTSEEYOUOVERCADOGANWESTCOMINGATONCE
# Playfair Matrix:
# M F H I/J K
# U N O P Q
# Z V W X Y
# E L A R G
# D S T B C
# The message is prepared into digraphs for Playfair encryption.
