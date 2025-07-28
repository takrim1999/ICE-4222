from louis import plain_text

KEY = 3

# This function is going to take a key and plaintext and return a ciphertext encrypted by that key
def encrypt(plaintext,key):
    ciphertext = []
    for letters in plaintext:
        ciphertext.append(chr((ord(letters) + key)%256))

    return "".join(ciphertext)

# This function is going to take a key and ciphertext and return a plaintext encrypted by that key
def decrypt(ciphertext,key):
    plaintext = []
    for cipherletter in ciphertext:
        plaintext.append(chr((ord(cipherletter)-key)%256))
    return "".join(plaintext)

# This function will brute force with multiple key and hacker would try to determine the currect key by looking at it.
def hack_by_bruteforce(ciphertext):
    for key in range(1,26):
        plaintext = []
        for cipherletter in ciphertext:
            plaintext.append(chr((ord(cipherletter) - key) % 256))
        print("Key: ",key,"Recovered Data: ", "".join(plaintext))
data = "Hello, World!"
encrypted_data = encrypt(data,KEY)
print("Data: ", data)
print("Encrypted Data: ", encrypted_data)
decrypted_data = decrypt(encrypted_data,KEY)
print("Decrypted Data: ", decrypted_data)
hack_by_bruteforce(encrypted_data)
