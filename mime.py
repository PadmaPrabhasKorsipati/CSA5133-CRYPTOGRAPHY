import base64

print("MIME Algorithm")
print("1. Encode")
print("2. Decode")

choice = int(input("Enter choice: "))

# ENCODE
if choice == 1:
    message = input("Enter message: ")

    encoded = base64.b64encode(message.encode())

    print("\nEncoded Message:", encoded.decode())


# DECODE
elif choice == 2:
    encoded_message = input("Enter encoded message: ")

    decoded = base64.b64decode(encoded_message.encode())

    print("\nDecoded Message:", decoded.decode())


else:
    print("Invalid choice")