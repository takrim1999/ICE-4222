import string
import random

def generate_key_map(iterations = 1):
    keymap = dict(enumerate(string.printable))
    for i in range(iterations):
        random.shuffle(keymap)
    return keymap

def swap_key_map(keymap):
    swapped_key_map = {}
    for i, j in keymap.items():
        swapped_key_map[j] = i
    return swapped_key_map

def encrypt(plain_text,secret_key_map):
    cipher_text = ""
    normal_key_map = generate_key_map(iterations=0)
    swapped_key_map =  swap_key_map(normal_key_map)
    for character in plain_text:
        cipher_text += secret_key_map[swapped_key_map[character]]
    return cipher_text

def decrypt(cipher_text, secret_key_map):
    plaintext = ""
    normal_key_map = generate_key_map(iterations=0)
    swapped_key_map = swap_key_map(secret_key_map)
    for character in cipher_text:
        plaintext += normal_key_map[swapped_key_map[character]]
    return plaintext

key_map = generate_key_map(random.randint(1,101))
plaintext = "Hello, World!"
encrypted_text = encrypt(plaintext,key_map)
decrypted_text = decrypt(encrypted_text, key_map)
print("Your Text: ", plaintext)
print("Shared Secret Keymap: ", key_map)
print("Encrypted Data: ", encrypted_text)
print("Decrypted Data: ", decrypted_text)
