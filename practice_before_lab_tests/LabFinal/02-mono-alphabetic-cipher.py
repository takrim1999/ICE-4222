import string
import random

def generate_key_maps(iterations = 0):
    key_map = enumerate(string.printable)
    key_map = dict(key_map)
    for i in range(iterations):
        random.shuffle(key_map)
    return key_map

def encrypt(text, map):
    normal_map = generate_key_maps()
    reverse_map = {}
    cipher = ""
    for i, j in normal_map.items():
        reverse_map[j] = i
    for char in text:
        cipher += map[reverse_map[char]]
    return cipher

def decrypt(cipher, map):
    text = ""
    normal_map = generate_key_maps()
    reverse_map = {}
    for i, j in map.items():
        reverse_map[j] = i
    for char in cipher:
        text += normal_map[reverse_map[char]]
    return text


plain_text = "Hello, World!"
random_key_map = generate_key_maps(5)
cipher_text = encrypt(plain_text, random_key_map)
recovered_text = decrypt(cipher_text, random_key_map)

print("Plain Text: ", plain_text)
print("Encrypting using key map: ", random_key_map)
print("Encrypted Text: ", cipher_text)
print("Decrypted Text: ", recovered_text)