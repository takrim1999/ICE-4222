# import numpy as np
import string

alphabates = string.ascii_lowercase
letter_matrix = []

# taking my keyword
keyword = "playfair"
plaintext = "there"
# pre processing matrix
for letter in keyword:
    if letter not in letter_matrix:
        letter_matrix.append(letter)
for letter in alphabates:
    if letter not in letter_matrix:
        if letter == "j":
            continue
        letter_matrix.append(letter)
matrix = []
while letter_matrix:
    matrix.append(letter_matrix[:5])
    letter_matrix = letter_matrix[5:]

letter_matrix = matrix[0:]
# print(letter_matrix)
for i in letter_matrix:
    print(i)

# processing plain text:
i = 0
text_pairs = []
flag = 0
while i < len(plaintext)-1:
    if plaintext[i] == plaintext[i+1]:
        flag += 1
        text_pairs.append([plaintext[i],"x"])
        i+=1
    else:
        text_pairs.append([plaintext[i],plaintext[i+1]])
        i+=2
if len(text_pairs)*2 < len(plaintext)+flag:
    text_pairs.append([plaintext[-1],"x"])
print(text_pairs)

ciphertext = []
for pair in text_pairs:
    print(pair[0], pair[1])
    for row in range(len(letter_matrix)):
        for col in range(len(letter_matrix)):
            if letter_matrix[row][col] == pair[0]:
                row0, col0 = row,col
            if letter_matrix[row][col] == pair[1]:
                row1, col1 = row, col
    if row0 == row1:
        col0  = (col0 + 1)%5
        col1 += (col1 + 1)%5
        ciphertext.append(letter_matrix[row0][col0])
        ciphertext.append(letter_matrix[row1][col1])
    elif col0 == col1:
        row0 = (row0 + 1)%5
        row1 = (row1 + 1)%5
        ciphertext.append(letter_matrix[row0][col0])
        ciphertext.append(letter_matrix[row1][col1])
    else:
        col0,col1 = col1,col0
        ciphertext.append(letter_matrix[row0][col0])
        ciphertext.append(letter_matrix[row1][col1])
    # print((row0,col0),(row1,col1))
print(ciphertext)