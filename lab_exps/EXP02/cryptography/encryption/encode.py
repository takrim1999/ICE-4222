with open("lab_exps/EXP02/cryptography/encryption/character_map.key", "r") as map:
    character_map = eval(map.read())

def encipher(text):
    
    print("Using Character Map:", character_map)
    cipher_text = ""
    for i in text:
        cipher_text += chr(character_map[ord(i)])

    with open("lab_exps/EXP02/cryptography/encryption/ciphertext.txt", "w") as cipher:
        cipher.write(cipher_text)
    return cipher_text

with open("lab_exps/EXP02/cryptography/encryption/plaintext.txt", "r") as file:
    text = file.read()
    print("Plain Text:", text)
    print("Cipher Text:", encipher(text))