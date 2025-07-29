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