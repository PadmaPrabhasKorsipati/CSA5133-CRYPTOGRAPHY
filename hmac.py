import hashlib

def generate_hmac(message, key):

    h = hashlib.sha256()

    data = key + message

    h.update(data.encode())

    return h.hexdigest()


print("HMAC Algorithm")
print("1. Encrypt")
print("2. Decrypt")

choice = int(input("Enter choice: "))


if choice == 1:

    message = input("Enter message: ")
    key = input("Enter secret key: ")

    mac = generate_hmac(message, key)

    print("Generated HMAC:", mac)


elif choice == 2:

    message = input("Enter message: ")
    key = input("Enter secret key: ")
    received_mac = input("Enter received HMAC: ")

    mac = generate_hmac(message, key)

    if mac == received_mac:
        print("HMAC verified successfully")
    else:
        print("HMAC verification failed")

else:
    print("Invalid choice")