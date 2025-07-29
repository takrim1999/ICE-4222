def encrypt(massage, shift):
    result = ""
    for char in massage:
        result += chr((ord(char) + shift) % 256)

    return result


def decryption(msg, k):
    result = ""
    for char in msg:
        result += chr((ord(char) - k) % 256)

    return result


def brturforce_decrypt(massage, shift):
    for a in range(1, 26):
        massag = decryption(massage, a)
        print(f"A{a}:{massag}")


massage = input("Give a massage to encrypt decrypt: ")
shift = int(input("write the shift for encrypt decrypt: "))
Encrypted = encrypt(massage, shift)

print("Your massage: ", massage)
print("Encrypted massage: ", Encrypted)

brturforce_decrypt(Encrypted, shift)

# with open('filename.txt', 'r') as file:
#   content = file.read()
#   print(content)
Shehab
import random
import string


def generate_key():
    letters = list(string.ascii_uppercase)
    shuffled = letters[:]
    random.shuffle(shuffled)
    return dict(zip(letters, shuffled))


def encrypt(plaintext, key):
    plaintext = plaintext.upper()
    ciphertext = ""
    for char in plaintext:
        if char in key:
            ciphertext += key[char]
        else:
            ciphertext += char
    return ciphertext


def decrypt(ciphertext, key):
    inverse_key = {v: k for k, v in key.items()}
    plaintext = ""
    for char in ciphertext:
        if char in inverse_key:
            plaintext += inverse_key[char]
        else:
            plaintext += char
    return plaintext


key = generate_key()
print("Cipher Key:", key)

message = "HELLO WORLD"
encrypted = encrypt(message, key)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)

# =============== Alternative Way ===============
# import random
# key = [chr(i) for i in range(65,91)]
# random.shuffle(key)

# plainText = "This Is A Text"
# plainText =  plainText.replace(" ","").upper()

# encryptedText = "".join([key[ord(c)-65] for c in plainText])
# print(encryptedText)

# decryptedText = "".join([chr(key.index(c)+65) for c in encryptedText])
# print(decryptedText)
Shehab


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd_val, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd_val, x, y


def generate_keys(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Give prime numbers: ")
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1
    , d, = extended_gcd(e, phi)
    d = d % phi
    return ((e, n), (d, n))


def encrypt(massage, public_key):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in massage]
    return cipher


def decrypt(cipher, privet_key):
    d, n = privet_key
    message = ''.join([chr(pow(char, d, n)) for char in cipher])
    return massage


p = int(input("Give the first prime number: "))
q = int(input("Give the Second prime number: "))
public_key, privet_key = generate_keys(p, q)

massage = input("Give a massage to encrypt: ")
encrypted = encrypt(massage, public_key)
decrypted = decrypt(encrypted, privet_key)

print("Public keys: ", public_key)
print("Pivet keys: ", privet_key)
print("Encrypted Massage: ", encrypted)
print("Decrypted Massage: ", decrypted)
Shehab


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
Shehab
import random


def findPrimitiveRoot(p):
    roots = []
    for q in range(2, p):
        results = []
        for i in range(1, p):
            r = pow(q, i, p)
            if r in results:
                break
            else:
                results.append(r)
        if len(results) == p - 1:
            roots.append(q)
    return roots


p = int(input("Enter Prime Number(P): "))
roots = findPrimitiveRoot(p)

print(f"Select a primitive root of {p} is {roots}")
g = 0
while (True):
    g = int(input("Select a number from the above list: "))
    if (g in roots):
        break
    print(f"{g} is not a primitive root of {p}. Try again")

# Key for A
Xa = random.randint(2, p - 1)
Ya = g ** Xa % p

# Key for B
Xb = random.randint(2, p - 1)
while (Xb == Xa):
    Xb = random.randint(2, p - 1)

Yb = g ** Xb % p

# Shared key for A & B
Ka = Yb ** Xa % p
Kb = Ya ** Xb % p

print(f"Secret for A: {Xa}")
print(f"Public for A: {Ya}")

print(f"Secret for B: {Xb}")
print(f"Public for B: {Yb}")

print(f"Shared key for A: {Ka}")
print(f"Shared key for B: {Kb}")
Shehab


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
Shehab


def encrypt_block(m, k):
    return (3 * (m + k)) % 16


def decrypt_block(c, k):
    return (11 * c - k) % 16


def ecb_encrypt(plain_blocks, key):
    return [encrypt_block(m, key) for m in plain_blocks]


def ecb_decrypt(cipher_blocks, key):
    return [decrypt_block(c, key) for c in cipher_blocks]


def cbc_encrypt(plain_blocks, key, iv):
    cipher_blocks = []
    prev = iv
    for m in plain_blocks:
        x = m ^ prev
        c = encrypt_block(x, key)
        cipher_blocks.append(c)
        prev = c
    return cipher_blocks


def cbc_decrypt(cipher_blocks, key, iv):
    plain_blocks = []
    prev = iv
    for c in cipher_blocks:
        x = decrypt_block(c, key)
        m = x ^ prev
        plain_blocks.append(m)
        prev = c
    return plain_blocks


def cfb_encrypt(plain_blocks, key, iv):
    cipher_blocks = []
    shift_register = iv
    for m in plain_blocks:
        o = encrypt_block(shift_register, key)
        c = m ^ o
        cipher_blocks.append(c)
        shift_register = c
    return cipher_blocks


def cfb_decrypt(cipher_blocks, key, iv):
    plain_blocks = []
    shift_register = iv
    for c in cipher_blocks:
        o = encrypt_block(shift_register, key)
        m = c ^ o
        plain_blocks.append(m)
        shift_register = c
    return plain_blocks


def ofb_encrypt(plain_blocks, key, iv):
    keystream = []
    o = iv
    for _ in plain_blocks:
        o = encrypt_block(o, key)
        keystream.append(o)
    return [m ^ k for m, k in zip(plain_blocks, keystream)]


def ofb_decrypt(cipher_blocks, key, iv):
    keystream = []
    o = iv
    for _ in cipher_blocks:
        o = encrypt_block(o, key)
        keystream.append(o)
    return [c ^ k for c, k in zip(cipher_blocks, keystream)]


def blocks_to_hex(blocks):
    return ''.join(f'{x:X}' for x in blocks)


if _name_ == "_main_":
    # Configuration
    key = 10  # 4-bit key (0-15)
    iv = 1  # 4-bit IV (0-15)
    plaintext_hex = "24"  # Two 4-bit blocks: ['2', '4']
    plain_blocks = [int(char, 16) for char in plaintext_hex]

    print(f"Plaintext: {plaintext_hex}")
    print(f"Key: {key} (0x{key:X})")
    print(f"IV: {iv} (0x{iv:X})\n")

    # ECB Mode
    ecb_cipher = ecb_encrypt(plain_blocks, key)
    ecb_decrypted = ecb_decrypt(ecb_cipher, key)
    print("ECB Mode:")
    print(f"  Ciphertext: {blocks_to_hex(ecb_cipher)}")
    print(f"  Decrypted: {blocks_to_hex(ecb_decrypted)}")

    # CBC Mode
    cbc_cipher = cbc_encrypt(plain_blocks, key, iv)
    cbc_decrypted = cbc_decrypt(cbc_cipher, key, iv)
    print("\nCBC Mode:")
    print(f"  Ciphertext: {blocks_to_hex(cbc_cipher)}")
    print(f"  Decrypted: {blocks_to_hex(cbc_decrypted)}")

    # CFB Mode
    cfb_cipher = cfb_encrypt(plain_blocks, key, iv)
    cfb_decrypted = cfb_decrypt(cfb_cipher, key, iv)
    print("\nCFB Mode:")
    print(f"  Ciphertext: {blocks_to_hex(cfb_cipher)}")
    print(f"  Decrypted: {blocks_to_hex(cfb_decrypted)}")

    # OFB Mode
    ofb_cipher = ofb_encrypt(plain_blocks, key, iv)
    ofb_decrypted = ofb_decrypt(ofb_cipher, key, iv)
    print("\nOFB Mode:")
    print(f"  Ciphertext: {blocks_to_hex(ofb_cipher)}")
    print(f"  Decrypted: {blocks_to_hex(ofb_decrypted)}")
Shehab
# Elliptic Curve Cryptography

p = int(input("Enter a Prime number,p: "))
a = int(input("Enter a coefficient a: "))
b = int(input("Enter a coefficient b: "))


def points_on_curve(a, b):
    affine_points = []
    n = 0
    for x in range(p):
        rhs = (x ** 3 + a * x + b) % p
        for y in range(p):
            if (y * y) % p == rhs:
                affine_points.append((x, y))
                n += 1
    return affine_points, n


print("affine points: ", points_on_curve(a, b))


def point_doubling(G):
    if G is None:
        return None

    x1, y1 = G

    if y1 == 0:
        return None

    s = (3 * x1 * x1 + a) * pow(2 * y1, -1, p) % p
    x3 = (s * s - 2 * x1) % p
    y3 = (s * (x1 - x3) - y1) % p

    return (x3, y3)


def point_addition(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2:
        if y1 != y2 or y1 == 0:
            return None

    if P == Q:
        return point_doubling(P)

    s = (y2 - y1) * pow(x2 - x1, -1, p) % p
    x3 = (s * s - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p
    return (x3, y3)


# Generator point input
# Gx = int(input("Enter x of generator point G: "))
# Gy = int(input("Enter y of generator point G: "))
# G = (Gx, Gy)

# print("1G = ",(G))

# print("2G = ", point_doubling(G))


def order_of_G(G):
    Q = G
    order = 1
    points_order = []
    print(f"{order}G: ", (Q))
    points_order.append(Q)
    while True:
        Q = point_addition(Q, G)
        order += 1

        if Q is None:
            print(f"{order}G: Identity (∞)")
            break

        print(f"{order}G: ", (Q))
        points_order.append(Q)
    return order, points_order


# n,points_order = order_of_G(G)
# print(n,points_order)

def max_order():
    affine_points, _ = points_on_curve(a, b)
    max_G = 0
    generatorPoint = None
    points_of_G_order = []

    for point in affine_points:
        print("Generator point: ", point)
        n, points = order_of_G(point)

        if n > max_G:
            generatorPoint = point
            points_of_G_order = points
            max_G = n

    return max_G, generatorPoint, points_of_G_order


# print("Order of Affine",max_order())

max_G, generatorPoint, points_of_G_order = max_order()

print(f"max_G: {max_G} \ngeneratorPoint: {generatorPoint}\n points_of_G_order: {points_of_G_order}")

# Key exchange Using ECC

# Private key of Bob 1<= B <= n-1

B = int(input("Enter a private key of Bob B: "))
A = int(input("Enter a private key of Alice A: "))

# Compute Public Key of Bob Pb = BG and Alice Pa = AG

Pb = points_of_G_order[B - 1]
Pa = points_of_G_order[A - 1]

print(Pa, Pb)

# Computes Bob's key
key_order1, key_points1 = order_of_G(Pa)

Kb = key_points1[B - 1]
print("Bob's key", Kb)

# Computes Alice's key
key_order2, key_points2 = order_of_G(Pb)

Ka = key_points2[A - 1]
print("Alice key", Ka)

# Encryption of ECC Cm = {AG , Pm + Ka}

P = (6, 3)  # Plaintext

Cm = (Pa, point_addition(P, Ka))  # Cipher text

# Decryption of ECC Pm = P + Ka - Kb
Pmx = P[0] + Ka[0] - Kb[0]
Pmy = P[1] + Ka[1] - Kb[1]

Pm = (Pmx, Pmy)

print("Cipher text and plaintext", Cm, Pm)