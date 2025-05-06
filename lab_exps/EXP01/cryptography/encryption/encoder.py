with open("EXP01/cryptography/encryption/shift.key",'r') as key:
    KEY = int(key.read().strip())

# print("Key: ", KEY)
def encipher(text,key):
    cipher_text = []
    for character in text:
        cipher_text.append(chr((ord(character)+key)%256))
        # print("".join(cipher_text))
    cipher_text = "".join(cipher_text)
    with open("EXP01/cryptography/encryption/cipher_text.txt", "w") as cipher:
        cipher.write(cipher_text)
    return cipher_text

with open("EXP01/cryptography/encryption/plaintext.txt", "r") as file:
    text = file.read()
    print(encipher(text,KEY))