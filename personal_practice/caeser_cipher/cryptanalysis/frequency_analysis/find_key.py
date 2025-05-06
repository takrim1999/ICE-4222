with open("personal_practice/caeser_cipher/cryptanalysis/frequency_analysis/cipher_text.txt","r") as file:
    cipher = file.read()
    # print("Theft Cipher: ", cipher)
# with open("EXP01/cryptanalysis/words.txt", "r") as word_file:
#     words = word_file.read().strip().split()


def find_frequency_dictionary(cipher):
    frequency_dictionary = {}
    for char in cipher:
        if char not in frequency_dictionary:
            frequency_dictionary[char] = 1
        else:
            frequency_dictionary[char] += 1
    return frequency_dictionary


print(find_frequency_dictionary(cipher))



# def test_key(cipher,possible_key):
#     possible_recovered_text = []
#     test_alpha_text = []
#     flag = True
#     for character in cipher:
#         possible_recovered_text.append(chr((ord(character)-possible_key)%256))        
#         if ord(character) == 32+possible_key:
#             flag = False
#         if flag and character.isalpha():
#             test_alpha_text.append(chr((ord(character)-possible_key)%256))
#         # print("".join(cipher_text))
#     possible_recovered_text = "".join(possible_recovered_text)
#     test_alpha_text = "".join(test_alpha_text)
#     if not flag:
#         if test_alpha_text.lower() in words:
#             print("detected word ", test_alpha_text)
#             print("Possible Key: ",  possible_key)
#             print("Possible recovered text: ", possible_recovered_text)
#             return True
#     # with open("EXP01/cryptography/decryption/recovered_text.txt","w") as recovered:
#     #     recovered.write(recovered_text)
#     return test_alpha_text, possible_recovered_text

# for possible_key in range(1,26):
#     test_key(cipher,possible_key)
    