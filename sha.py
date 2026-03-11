def simple_sha(message):

    h = 0

    for ch in message:

        h = (h << 5) + h + ord(ch)   # hash calculation
        h = h % (2**32)              # keep 32-bit size

    return h


print("SHA Algorithm")
print("1. Encrypt")
print("2. Decrypt")

choice = int(input("Enter choice: "))


if choice == 1:

    message = input("Enter message: ")

    hash_value = simple_sha(message)

    print("Generated Hash:", hash_value)


elif choice == 2:

    message = input("Enter message: ")

    received_hash = int(input("Enter received hash: "))

    hash_value = simple_sha(message)

    if hash_value == received_hash:
        print("Hash verified successfully")
    else:
        print("Hash verification failed")

else:
    print("Invalid choice")