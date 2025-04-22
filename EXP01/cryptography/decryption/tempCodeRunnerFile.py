def decipher(text,key):
    recovered_text = []
    for character in text:
        recovered_text.append(chr((ord(character)-key)%256))
        # print("".join(cipher_text))
    recovered_text = "".join(recovered_text)
    with open("EXP01/cryptography/decryption/recovered_text.txt","w") as recovered:
        recovered.write(recovered_text)
    return recovered_text