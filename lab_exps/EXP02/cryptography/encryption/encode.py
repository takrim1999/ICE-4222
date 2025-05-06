import string
import random
letters = string.ascii_lowercase + " "
def encipher(text):
    character_map = {}
    for c in text:
        if c not in character_map:
            character_map[c] = letters[random.choice([i for i in range(27) if i != letters.index(c)])]
    print("Using Random Character Map:", character_map)
    cipher_text = ""
    for i in text:
        cipher_text += character_map[i]

    with open("lab_exps/EXP02/cryptography/encryption/ciphertext.txt", "w") as cipher:
        cipher.write(cipher_text)
    return cipher_text

with open("lab_exps/EXP02/cryptography/encryption/plaintext.txt", "r") as file:
    text = file.read()
    print(encipher(text))