with open("personal_practice/caeser_cipher/cryptography/decryption/shift.key",'r') as key:
    KEY = int(key.read().strip())

def decipher(text,key):
    recovered_text = []
    for character in text:
        recovered_text.append(chr((ord(character)-key)%256))
        # print("".join(cipher_text))
    recovered_text = "".join(recovered_text)
    with open("personal_practice/caeser_cipher/cryptography/decryption/recovered_text.txt","w") as recovered:
        recovered.write(recovered_text)
    return recovered_text

with open("personal_practice/caeser_cipher/cryptography/decryption/cipher_text.txt","r") as file:
    cipher = file.read()
    print(decipher(cipher,KEY))