import string
import numpy as np


def preprocess_text(text):
    """Convert text to uppercase and remove non-alphabetic characters."""
    clean_text = ''.join(filter(str.isalpha, text.upper()))
    return clean_text


def char_to_num(char):
    """Convert character to number (A=0, B=1, ..., Z=25)."""
    return ord(char) - ord('A')


def num_to_char(num):
    """Convert number to character (0=A, 1=B, ..., 25=Z)."""
    return chr(num + ord('A'))


def text_to_nums(text):
    """Convert text to list of numbers."""
    return [char_to_num(c) for c in text]


def nums_to_text(nums):
    """Convert list of numbers to text."""
    return ''.join(num_to_char(n) for n in nums)


def get_key_matrix(key, size=2):
    """
    Convert key string to a square matrix of given size.
    Args:
        key: string of key (must have at least size*size characters)
        size: dimension of the square matrix (default 2 for 2x2)
    Returns:
        key_matrix: numpy array of shape (size, size)
    """
    key_clean = preprocess_text(key)
    nums = text_to_nums(key_clean)

    # Pad key if needed with 'A' (0)
    while len(nums) < size * size:
        nums.append(0)

    # Create matrix and reshape
    key_matrix = np.array(nums[:size * size]).reshape(size, size)
    return key_matrix


def encrypt(plaintext, key, matrix_size=2):
    """
    Encrypt plaintext using Hill cipher.
    Args:
        plaintext: text to encrypt
        key: encryption key string
        matrix_size: size of the key matrix (default 2)
    Returns:
        ciphertext: encrypted string
    """
    # Preprocess and convert to numbers
    text_clean = preprocess_text(plaintext)

    # Pad text with 'X' if length not multiple of matrix_size
    padding = (matrix_size - len(text_clean) % matrix_size) % matrix_size
    if padding:
        text_clean += 'X' * padding

    nums = text_to_nums(text_clean)
    key_matrix = get_key_matrix(key, matrix_size)

    # Encrypt in blocks
    cipher_nums = []
    for i in range(0, len(nums), matrix_size):
        block = np.array(nums[i:i + matrix_size])
        encrypted_block = np.dot(key_matrix, block) % 26
        cipher_nums.extend(encrypted_block)

    return nums_to_text(cipher_nums)


def mod_inv(a, m=26):
    """Find modular multiplicative inverse of a mod m."""
    for inv in range(1, m):
        if (a * inv) % m == 1:
            return inv
    raise ValueError(f"{a} has no multiplicative inverse mod {m}")


def matrix_mod_inv(matrix, mod=26):
    """Calculate modular inverse of a matrix."""
    det = int(round(np.linalg.det(matrix)))
    det_inv = mod_inv(det % mod, mod)

    # Calculate adjugate matrix
    matrix_inv = np.linalg.inv(matrix) * det
    adjugate = np.round(matrix_inv).astype(int) % mod

    # Handle negative values
    adjugate[adjugate < 0] += mod

    # Multiply by modular inverse of determinant
    inv_matrix = (adjugate * det_inv) % mod
    return inv_matrix


def decrypt(ciphertext, key, matrix_size=2):
    """
    Decrypt ciphertext using Hill cipher.
    Args:
        ciphertext: text to decrypt
        key: decryption key string
        matrix_size: size of the key matrix (default 2)
    Returns:
        plaintext: decrypted string
    """
    # Preprocess and convert to numbers
    text_clean = preprocess_text(ciphertext)
    nums = text_to_nums(text_clean)
    key_matrix = get_key_matrix(key, matrix_size)

    # Calculate inverse matrix
    inv_matrix = matrix_mod_inv(key_matrix)

    # Decrypt in blocks
    plain_nums = []
    for i in range(0, len(nums), matrix_size):
        block = np.array(nums[i:i + matrix_size])
        decrypted_block = np.dot(inv_matrix, block) % 26
        plain_nums.extend(np.round(decrypted_block).astype(int))

    return nums_to_text(plain_nums)


# Example usage
if __name__ == "__main__":
    key = "hill"
    plain_text = "Hello, World!"

    # Encrypt
    cipher_text = encrypt(plain_text, key)

    # Decrypt
    decrypted_text = decrypt(cipher_text, key)

    print("Original text:", plain_text)
    print("Encrypted:   ", cipher_text)
    print("Decrypted:   ", decrypted_text)