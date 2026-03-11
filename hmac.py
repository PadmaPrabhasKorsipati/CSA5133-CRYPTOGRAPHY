def simple_hash(text):

    h = 0

    for ch in text:
        h = (h + ord(ch)) % 256

    return h


def generate_hmac(message, key):

    inner = key + message
    inner_hash = simple_hash(inner)

    outer = key + str(inner_hash)
    hmac = simple_hash(outer)

    return hmac


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
    received_mac = int(input("Enter received HMAC: "))

    mac = generate_hmac(message, key)

    if mac == received_mac:
        print("HMAC verified successfully")
    else:
        print("HMAC verification failed")

else:
    print("Invalid choice")