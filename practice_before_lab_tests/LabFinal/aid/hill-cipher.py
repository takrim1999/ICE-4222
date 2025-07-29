def mod_inverse(a, m):
    # Find modular inverse of a under mod m
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise ValueError("No modular inverse exists")


def get_key_matrix(key):
    key = key.upper().replace(" ", "")
    if len(key) != 4:
        raise ValueError("Key must be 4 letters for 2x2 matrix")

    key_matrix = [[0] * 2 for _ in range(2)]
    k = 0
    for i in range(2):
        for j in range(2):
            key_matrix[i][j] = ord(key[k]) % 65
            k += 1
    return key_matrix


def matrix_inverse(matrix):
    # Calculate determinant
    det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 26
    det_inv = mod_inverse(det, 26)

    # Adjugate matrix
    adj = [
        [matrix[1][1], (-matrix[0][1]) % 26],
        [(-matrix[1][0]) % 26, matrix[0][0]]
    ]

    # Multiply adjugate by det_inv mod 26
    inv_matrix = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            inv_matrix[i][j] = (det_inv * adj[i][j]) % 26
    return inv_matrix


def encrypt(message, key_matrix):
    message = message.upper().replace(" ", "")
    if len(message) % 2 != 0:
        message += 'X'  # Padding if needed

    cipher_text = ""

    for i in range(0, len(message), 2):
        vector = [ord(message[i]) % 65, ord(message[i + 1]) % 65]

        result = [0, 0]
        for j in range(2):
            result[j] = (key_matrix[j][0] * vector[0] + key_matrix[j][1] * vector[1]) % 26

        cipher_text += chr(result[0] + 65) + chr(result[1] + 65)
    return cipher_text


def decrypt(cipher_text, key_matrix):
    cipher_text = cipher_text.upper().replace(" ", "")
    if len(cipher_text) % 2 != 0:
        raise ValueError("Cipher text length must be even")

    inv_key_matrix = matrix_inverse(key_matrix)

    decrypted_text = ""

    for i in range(0, len(cipher_text), 2):
        vector = [ord(cipher_text[i]) % 65, ord(cipher_text[i + 1]) % 65]

        result = [0, 0]
        for j in range(2):
            result[j] = (inv_key_matrix[j][0] * vector[0] + inv_key_matrix[j][1] * vector[1]) % 26

        decrypted_text += chr(result[0] + 65) + chr(result[1] + 65)
    return decrypted_text


# ========== MAIN PROGRAM ==========
key = input("Enter 4-letter key (e.g. HILL): ")
message = input("Enter message to encrypt: ")

try:
    key_matrix = get_key_matrix(key)
    cipher_text = encrypt(message, key_matrix)
    decrypted_text = decrypt(cipher_text, key_matrix)

    print("\n🔐 Encrypted message:", cipher_text)
    print("🔓 Decrypted message:", decrypted_text)

except Exception as e:
    print("Error:", e)