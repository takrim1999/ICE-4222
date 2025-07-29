import random
import string


def generate_key():
    letters = list(string.ascii_uppercase)
    shuffled = letters[:]
    random.shuffle(shuffled)
    return dict(zip(letters, shuffled))


def encrypt(plaintext, key):
    plaintext = plaintext.upper()
    ciphertext = ""
    for char in plaintext:
        if char in key:
            ciphertext += key[char]
        else:
            ciphertext += char
    return ciphertext


def decrypt(ciphertext, key):
    inverse_key = {v: k for k, v in key.items()}
    plaintext = ""
    for char in ciphertext:
        if char in inverse_key:
            plaintext += inverse_key[char]
        else:
            plaintext += char
    return plaintext


key = generate_key()
print("Cipher Key:", key)

message = "HELLO WORLD"
encrypted = encrypt(message, key)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)

# =============== Alternative Way ===============
# import random
# key = [chr(i) for i in range(65,91)]
# random.shuffle(key)

# plainText = "This Is A Text"
# plainText =  plainText.replace(" ","").upper()

# encryptedText = "".join([key[ord(c)-65] for c in plainText])
# print(encryptedText)

# decryptedText = "".join([chr(key.index(c)+65) for c in encryptedText])
# print(decryptedText)