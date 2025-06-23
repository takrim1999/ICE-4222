text = "a quick brown fox jumps over a lazy dog"
frequency = {}
for letter in text:
    if letter in frequency:
        frequency[letter] += 1
    else:
        frequency[letter] = 1

print(frequency)