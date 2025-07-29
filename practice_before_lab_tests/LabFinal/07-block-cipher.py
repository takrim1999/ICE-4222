import struct

BLOCK_SIZE = 8  # bytes
PAD_CHAR = '\x00'


def str_to_bytes(s):
    return s.encode('utf-8')


def bytes_to_str(b):
    return b.decode('utf-8', errors='ignore')


def pad(s):
    pad_len = BLOCK_SIZE - (len(s) % BLOCK_SIZE)
    return s + (PAD_CHAR * pad_len)


def split_blocks(data_bytes):
    return [data_bytes[i:i + BLOCK_SIZE] for i in range(0, len(data_bytes), BLOCK_SIZE)]


def xor_block_visual(block1, block2):
    result = bytes(a ^ b for a, b in zip(block1, block2))

    # Binary visualization
    print(" Block A: ", ' '.join(f'{b:08b}' for b in block1))
    print(" Block B: ", ' '.join(f'{b:08b}' for b in block2))
    print("   XOR   : ", ' '.join(f'{b:08b}' for b in result))
    print(" XOR TXT: ", bytes_to_str(result))
    print('-' * 80)

    return result


# ECB Mode with visualization
def encrypt_ecb(plaintext, key_str):
    print("=== ECB ENCRYPT ===")
    plaintext = pad(plaintext)
    plaintext_bytes = str_to_bytes(plaintext)
    key = str_to_bytes(key_str)[:BLOCK_SIZE]

    blocks = split_blocks(plaintext_bytes)
    ciphertext = b''
    for block in blocks:
        ciphertext += xor_block_visual(block, key)
    return ciphertext


def decrypt_ecb(ciphertext, key_str):
    print("=== ECB DECRYPT ===")
    key = str_to_bytes(key_str)[:BLOCK_SIZE]
    blocks = split_blocks(ciphertext)
    decrypted = b''
    for block in blocks:
        decrypted += xor_block_visual(block, key)
    return bytes_to_str(decrypted).rstrip(PAD_CHAR)


# CTR Mode with visualization
def encrypt_ctr(plaintext, key_str, nonce_str):
    print("=== CTR ENCRYPT ===")
    plaintext = pad(plaintext)
    plaintext_bytes = str_to_bytes(plaintext)
    key = str_to_bytes(key_str)[:BLOCK_SIZE]
    nonce = str_to_bytes(nonce_str)[:BLOCK_SIZE]

    blocks = split_blocks(plaintext_bytes)
    ciphertext = b''

    for i, block in enumerate(blocks):
        counter = struct.pack('>Q', i)
        nonce_counter = bytes(a ^ b for a, b in zip(nonce, counter))
        keystream = xor_block_visual(nonce_counter, key)
        encrypted = xor_block_visual(block, keystream)
        ciphertext += encrypted

    return ciphertext


def decrypt_ctr(ciphertext, key_str, nonce_str):
    print("=== CTR DECRYPT ===")
    key = str_to_bytes(key_str)[:BLOCK_SIZE]
    nonce = str_to_bytes(nonce_str)[:BLOCK_SIZE]
    blocks = split_blocks(ciphertext)
    plaintext = b''

    for i, block in enumerate(blocks):
        counter = struct.pack('>Q', i)
        nonce_counter = bytes(a ^ b for a, b in zip(nonce, counter))
        keystream = xor_block_visual(nonce_counter, key)
        decrypted = xor_block_visual(block, keystream)
        plaintext += decrypted

    return bytes_to_str(plaintext).rstrip(PAD_CHAR)


plaintext = "Hello XOR World!"
key = "mysecret"
nonce = "NONCE123"

# ECB
ciphertext_ecb = encrypt_ecb(plaintext, key)
decrypted_ecb = decrypt_ecb(ciphertext_ecb, key)
print("ECB Decrypted:", decrypted_ecb)

# CTR
ciphertext_ctr = encrypt_ctr(plaintext, key, nonce)
decrypted_ctr = decrypt_ctr(ciphertext_ctr, key, nonce)
print("CTR Decrypted:", decrypted_ctr)
