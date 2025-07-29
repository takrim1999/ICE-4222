import string


def construct_matrix(key):
    character_order_list = []
    matrix = []
    for char in key:
        if char.upper() not in character_order_list:
            character_order_list.append(char.upper())
    for char in string.ascii_uppercase:
        if char not in character_order_list:
            if char == "I" and "J" in character_order_list:
                continue
            if char == "J" and "I" in character_order_list:
                continue
            character_order_list.append(char)
    for i in range(0, 25, 5):
        matrix.append(character_order_list[i:i + 5])
    return matrix


def get_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return (i, j)
    return None


def encrypt(text, key):
    # Preprocess text: uppercase, remove non-alpha, replace J with I
    clean_text = ''.join(filter(str.isalpha, text.upper())).replace('J', 'I')
    encryption_matrix = construct_matrix(key)

    # Form digraphs
    pairs = []
    i = 0
    while i < len(clean_text):
        if i == len(clean_text) - 1:
            pairs.append(clean_text[i] + 'X')
            i += 1
        elif clean_text[i] == clean_text[i + 1]:
            pairs.append(clean_text[i] + 'X')
            i += 1
        else:
            pairs.append(clean_text[i] + clean_text[i + 1])
            i += 2

    # Encrypt each digraph
    cipher_text = ""
    for pair in pairs:
        a, b = pair[0], pair[1]
        row1, col1 = get_position(encryption_matrix, a)
        row2, col2 = get_position(encryption_matrix, b)

        if row1 == row2:  # Same row
            new_col1 = (col1 + 1) % 5
            new_col2 = (col2 + 1) % 5
            cipher_text += encryption_matrix[row1][new_col1] + encryption_matrix[row2][new_col2]
        elif col1 == col2:  # Same column
            new_row1 = (row1 + 1) % 5
            new_row2 = (row2 + 1) % 5
            cipher_text += encryption_matrix[new_row1][col1] + encryption_matrix[new_row2][col2]
        else:  # Rectangle
            cipher_text += encryption_matrix[row1][col2] + encryption_matrix[row2][col1]

    return cipher_text


def decrypt(cipher_text, key):
    # Preprocess: ensure uppercase and valid
    cipher_clean = ''.join(filter(str.isalpha, cipher_text.upper()))
    decryption_matrix = construct_matrix(key)

    # Form digraphs
    pairs = []
    for i in range(0, len(cipher_clean), 2):
        pairs.append(cipher_clean[i:i + 2])

    # Decrypt each digraph
    plain_text = ""
    for pair in pairs:
        a, b = pair[0], pair[1]
        row1, col1 = get_position(decryption_matrix, a)
        row2, col2 = get_position(decryption_matrix, b)

        if row1 == row2:  # Same row
            new_col1 = (col1 - 1) % 5
            new_col2 = (col2 - 1) % 5
            plain_text += decryption_matrix[row1][new_col1] + decryption_matrix[row2][new_col2]
        elif col1 == col2:  # Same column
            new_row1 = (row1 - 1) % 5
            new_row2 = (row2 - 1) % 5
            plain_text += decryption_matrix[new_row1][col1] + decryption_matrix[new_row2][col2]
        else:  # Rectangle
            plain_text += decryption_matrix[row1][col2] + decryption_matrix[row2][col1]

    return plain_text


# Example usage
key = "monarchy"
plain_text = "Hello, World!"
cipher_text = encrypt(plain_text, key)
decrypted_text = decrypt(cipher_text, key)

print("Your plain text: ", plain_text)
print("Your cipher text: ", cipher_text)
print("Decrypted text: ", decrypted_text)