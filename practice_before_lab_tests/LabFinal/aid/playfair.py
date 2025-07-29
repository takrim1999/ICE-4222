def generate_key_matrix(key):
    key = key.upper().replace('J', 'I')
    matrix = []
    used = set()

    for char in key:
        if char.isalpha() and char not in used:
            matrix.append(char)
            used.add(char)

    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char not in used:
            matrix.append(char)
            used.add(char)

    key_matrix = [matrix[i:i + 5] for i in range(0, 25, 5)]
    return key_matrix


def format_plaintext(plaintext):
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    formatted = []
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        b = ''
        if i + 1 < len(plaintext):
            b = plaintext[i + 1]
        else:
            b = 'X'

        if a == b:
            formatted.append(a + 'X')
            i += 1
        else:
            formatted.append(a + b)
            i += 2

    if len(formatted[-1]) == 1:
        formatted[-1] += 'X'

    return formatted


def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None, None


def playfair_encrypt(plaintext, key):
    matrix = generate_key_matrix(key)
    pairs = format_plaintext(plaintext)
    ciphertext = ''

    for pair in pairs:
        a, b = pair[0], pair[1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    return ciphertext


def playfair_decrypt(ciphertext, key):
    matrix = generate_key_matrix(key)
    plaintext = ''

    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]

    return plaintext


# উদাহরণ চালনা
key = "MONARCHY"
plaintext = "INSTRUMENTS"

ciphertext = playfair_encrypt(plaintext, key)
decrypted = playfair_decrypt(ciphertext, key)

# প্রিন্ট আউট
print("Key Matrix:")
for row in generate_key_matrix(key):
    print(row)

print("\nOriginal Plaintext :", plaintext)
print("Encrypted Ciphertext:", ciphertext)
print("Decrypted Plaintext :", decrypted)