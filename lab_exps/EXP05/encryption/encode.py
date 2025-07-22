import string
from math import gcd

letters = string.ascii_lowercase
char_to_index = {char: idx for idx, char in enumerate(letters)}
index_to_char = {idx: char for char, idx in char_to_index.items()}


def create_key_matrix(key_text):

    cleaned_key = ''.join(filter(str.isalpha, key_text)).lower()
    if not cleaned_key:
        raise ValueError("Key contains no valid letters")

    if len(cleaned_key) < 9:
        cleaned_key += 'x' * (9 - len(cleaned_key))
    else:
        cleaned_key = cleaned_key[:9]

    key_matrix = []
    for i in range(0, 9, 3):
        row = [
            char_to_index[cleaned_key[i]],
            char_to_index[cleaned_key[i + 1]],
            char_to_index[cleaned_key[i + 2]]
        ]
        key_matrix.append(row)

    return key_matrix


def matrix_determinant(matrix):
    """Calculate determinant of a 3x3 matrix manually"""
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def is_invertible(matrix):
    """Check if matrix is invertible modulo 26"""
    det = matrix_determinant(matrix)
    det_mod = det % 26

    return det_mod != 0 and gcd(det_mod, 26) == 1


def encrypt(plaintext, keyMatrix):
    cleaned_text = ''.join(filter(str.isalpha, plaintext)).lower()
    if not cleaned_text:
        return ""

    pad_len = (3 - len(cleaned_text) % 3) % 3
    cleaned_text += 'x' * pad_len

    ciphertext = []
    for i in range(0, len(cleaned_text), 3):
        block = cleaned_text[i:i + 3]
        vector = [char_to_index[c] for c in block]
        result = [0, 0, 0]

        for row in range(3):
            total = 0
            for col in range(3):
                total += keyMatrix[row][col] * vector[col]
            result[row] = total % 26

        ciphertext.extend(index_to_char[idx] for idx in result)

    return ''.join(ciphertext)


with open("key.txt", "r") as key_file:
    key_text = key_file.read().strip()

with open("plaintext.txt", "r") as text_file:
    plaintext = text_file.read().strip()

try:
    key_matrix = create_key_matrix(key_text)

    if not is_invertible(key_matrix):
        print("Error: Key is incompatible, please use a different key")
        print("Generated key matrix:", key_matrix)
        exit(1)

    cipher_text = encrypt(plaintext, key_matrix)
    with open("cipher.txt", "w") as cipher_file:
        cipher_file.write(cipher_text)
    print("Ciphertext:", cipher_text)

except ValueError as e:
    print(f"Error: {e}")
    exit(1)