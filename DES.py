# Permutation tables
IP = [58,50,42,34,26,18,10,2,
      60,52,44,36,28,20,12,4,
      62,54,46,38,30,22,14,6,
      64,56,48,40,32,24,16,8,
      57,49,41,33,25,17,9,1,
      59,51,43,35,27,19,11,3,
      61,53,45,37,29,21,13,5,
      63,55,47,39,31,23,15,7]

FP = [40,8,48,16,56,24,64,32,
      39,7,47,15,55,23,63,31,
      38,6,46,14,54,22,62,30,
      37,5,45,13,53,21,61,29,
      36,4,44,12,52,20,60,28,
      35,3,43,11,51,19,59,27,
      34,2,42,10,50,18,58,26,
      33,1,41,9,49,17,57,25]

E = [32,1,2,3,4,5,
     4,5,6,7,8,9,
     8,9,10,11,12,13,
     12,13,14,15,16,17,
     16,17,18,19,20,21,
     20,21,22,23,24,25,
     24,25,26,27,28,29,
     28,29,30,31,32,1]

P = [16,7,20,21,
     29,12,28,17,
     1,15,23,26,
     5,18,31,10,
     2,8,24,14,
     32,27,3,9,
     19,13,30,6,
     22,11,4,25]

SBOX = [
[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
 [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
 [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
 [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],

[[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
 [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
 [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
 [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
]

# Utility functions
def permute(block, table):
    return "".join(block[i-1] for i in table)

def xor(a,b):
    return "".join('0' if i==j else '1' for i,j in zip(a,b))

def left_shift(k,n):
    return k[n:]+k[:n]

# Feistel function
def feistel(r,key):
    r_exp = permute(r,E)
    x = xor(r_exp,key)
    s_out=""
    for i in range(0,12,6):
        row=int(x[i]+x[i+5],2)
        col=int(x[i+1:i+5],2)
        val=SBOX[i//6][row][col]
        s_out+=format(val,'04b')
    return permute(s_out,P)

# Key generation (simplified)
def generate_keys(key):
    keys=[]
    k=key[:48]
    for i in range(16):
        k=left_shift(k,1)
        keys.append(k[:48])
    return keys

def des_process(text,key,mode):

    keys=generate_keys(key)

    if mode=="decrypt":
        keys=keys[::-1]

    text=permute(text,IP)

    L=text[:32]
    R=text[32:]

    for i in range(16):
        f=feistel(R,keys[i])
        newR=xor(L,f)
        L=R
        R=newR

    combined=R+L
    return permute(combined,FP)


# ---------------- Main Program ----------------

print("DES Algorithm")
print("1. Encrypt")
print("2. Decrypt")

choice=input("Enter choice: ")

text=input("Enter 64-bit binary text: ")
key=input("Enter 48-bit binary key: ")

if choice=="1":
    cipher=des_process(text,key,"encrypt")
    print("Encrypted:",cipher)

elif choice=="2":
    plain=des_process(text,key,"decrypt")
    print("Decrypted:",plain)

else:
    print("Invalid choice")