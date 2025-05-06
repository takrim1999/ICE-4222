with open("lab_exps/EXP02/cryptography/decryption/character_map.key", "r") as map:
    character_map = eval(map.read())

with open("lab_exps/EXP02/cryptography/decryption/ciphertext.txt", "r") as cipher:
    cipher_text = cipher.read()

def decode(cipher_text):
    swapped_map = {j:i for i,j in character_map.items()}
    print("Using Key Map", swapped_map)
    recovered_text = ""
    for char in cipher_text:
        recovered_text += chr(swapped_map[ord(char)])
    print("Recovered Text:", recovered_text)

decode(cipher_text)