import string
from math import gcd

letters = string.ascii_lowercase
char_to_index = {char: idx for idx, char in enumerate(letters)}
index_to_char = {idx: char for char, idx in char_to_index.items()}


def create_key_matrix(key_text):
    """Create a 3x3 key matrix from key text"""
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
    """Calculate determinant of a 3x3 matrix"""
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def is_invertible(matrix):
    """Check if matrix is invertible modulo 26"""
    det = matrix_determinant(matrix)
    det_mod = det % 26
    return det_mod != 0 and gcd(det_mod, 26) == 1


def mod_inverse(a, m=26):
    """Find modular inverse of a modulo m"""
    for inv in range(1, m):
        if (a * inv) % m == 1:
            return inv
    return None  # Should never happen for invertible matrices


def matrix_inverse(matrix):
    """Calculate inverse matrix modulo 26"""
    det = matrix_determinant(matrix)
    det_mod = det % 26
    det_inv = mod_inverse(det_mod, 26)

    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    # Calculate adjugate matrix with cofactors
    adjugate = [
        [e * i - f * h, c * h - b * i, b * f - c * e],
        [f * g - d * i, a * i - c * g, c * d - a * f],
        [d * h - e * g, g * b - a * h, a * e - b * d]
    ]

    # Multiply by det_inv and apply modulo 26
    inv_matrix = []
    for row in adjugate:
        inv_row = []
        for val in row:
            # Handle negative values before mod
            inv_val = (val * det_inv) % 26
            if inv_val < 0:
                inv_val += 26
            inv_row.append(inv_val % 26)
        inv_matrix.append(inv_row)

    return inv_matrix


def decrypt(ciphertext, inv_matrix):
    """Decrypt ciphertext using inverse matrix"""
    cleaned_cipher = ''.join(filter(str.isalpha, ciphertext)).lower()
    if not cleaned_cipher:
        return ""

    # Process in 3-character blocks
    plaintext = []
    for i in range(0, len(cleaned_cipher), 3):
        block = cleaned_cipher[i:i + 3]
        vector = [char_to_index[c] for c in block]
        result = [0, 0, 0]

        # Matrix multiplication with inverse matrix
        for row in range(3):
            total = 0
            for col in range(3):
                total += inv_matrix[row][col] * vector[col]
            result[row] = total % 26

        # Convert to plaintext
        plaintext.extend(index_to_char[idx] for idx in result)

    return ''.join(plaintext)


# Read key and ciphertext
with open("key.txt", "r") as key_file:
    key_text = key_file.read().strip()

with open("cipher.txt", "r") as cipher_file:
    ciphertext = cipher_file.read().strip()

# Create and validate key matrix
try:
    key_matrix = create_key_matrix(key_text)

    if not is_invertible(key_matrix):
        print("Error: Key matrix is not invertible modulo 26.")
        print("Please use the original key that was used for encryption.")
        exit(1)

    # Compute inverse matrix for decryption
    inv_matrix = matrix_inverse(key_matrix)

    # Decrypt and output
    plain_text = decrypt(ciphertext, inv_matrix)
    with open("recovered.txt", "w") as recovered_file:
        recovered_file.write(plain_text)
    print("Decrypted plaintext:", plain_text)

except ValueError as e:
    print(f"Error: {e}")
    exit(1)