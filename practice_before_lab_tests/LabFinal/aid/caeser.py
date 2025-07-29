def encrypt(massage, shift):
    result = ""
    for char in massage:
        result += chr((ord(char) + shift) % 256)

    return result


def decryption(msg, k):
    result = ""
    for char in msg:
        result += chr((ord(char) - k) % 256)

    return result


def brturforce_decrypt(massage, shift):
    for a in range(1, 26):
        massag = decryption(massage, a)
        print(f"A{a}:{massag}")


massage = input("Give a massage to encrypt decrypt: ")
shift = int(input("write the shift for encrypt decrypt: "))
Encrypted = encrypt(massage, shift)

print("Your massage: ", massage)
print("Encrypted massage: ", Encrypted)

brturforce_decrypt(Encrypted, shift)

# with open('filename.txt', 'r') as file:
#   content = file.read()
#   print(content)