def encrypt(text,key):
    result=" "
    j=0
    
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                start=65
            else:
                start=97
            shift=ord(key[j%len(key)].upper())-65
            result+=chr((ord(ch)-start+shift)%26 +start)
            j+=1
        else:
            result+=ch
    
    return result
        
def decrypt(text,key):
    result=" "
    j=0
    for ch in text:
        
        if ch.isalpha():
            if ch.isupper():
                start=65
            else:
                start=97
            shift=ord(key[j%len(key)].upper())-65
            result+=chr((ord(ch)-start-shift)%26 +start)
            j+=1
        else:
            result+=ch
    
    return result
        
        
        
print("Vigenere Cipher")
print("Choice:\n1.Encrypt\n2.Decrypt")
choice=int(input("Enter the choice:"))
text=input("Enter the text:")
key=input("Enter the key:")

if choice==1:
    cipher=encrypt(text,key)
    print(f"Encrypted Cipher Text:{cipher}")
elif choice==2:
    plain=decrypt(text,key)
    print(f"Decrypted Plain text:{plain}")
    
else:
    print("Invalid Input.")
    
        

