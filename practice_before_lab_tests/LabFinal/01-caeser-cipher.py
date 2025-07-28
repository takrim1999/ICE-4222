def encrypt(text,key=3):
    cipher = ""
    for char in text:
        cipher += chr((ord(char) + key)%256)
    return cipher

def decrypt(cipher,key=3):
    text = ""
    for char in cipher:
        text += chr((ord(char) - key) % 256)
    return text

def cryptanalysis(cipher):
    for key in range(26):
        text = ""
        for char in cipher:
            text += chr((ord(char)-key)%256)
        print(key , text)
    key = int(input("which key decryption can you read?\n>"))
    text = ""
    for char in cipher:
        text += chr((ord(char) - key) % 256)
    return key, text

KEY = 22

plain_text = "Hello, World!"
cipher_text = encrypt(plain_text,KEY)
decrypted_text = decrypt(cipher_text,KEY)
retrieved_key, recovered_text = cryptanalysis(cipher_text)
print("Plain Text: ", plain_text)
print("Cipher Text: ", cipher_text)
print("Recovered Text: ", decrypted_text)
print("Retrived Key: ", retrieved_key)
print("Recovered Text: ", recovered_text)
