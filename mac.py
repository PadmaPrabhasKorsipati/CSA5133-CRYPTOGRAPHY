def generate_mac(message, key):

    mac = ""

    for i in range(len(message)):

        if message[i] == key[i]:
            mac += "0"
        else:
            mac += "1"

    return mac


print("Message Authentication Code (MAC)")
print("1. Encrypt")
print("2. Decrypt")

choice = int(input("Enter choice: "))


if choice == 1:

    message = input("Enter binary message: ")
    key = input("Enter secret key: ")

    mac = generate_mac(message, key)

    print("Generated MAC:", mac)


elif choice == 2:

    message = input("Enter message: ")
    key = input("Enter secret key: ")
    received_mac = input("Enter received MAC: ")

    mac = generate_mac(message, key)

    if mac == received_mac:
        print("MAC verified successfully")
    else:
        print("MAC verification failed")


else:
    print("Invalid choice")