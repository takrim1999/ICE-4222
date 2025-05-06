import random
character_range = range(32,127)
character_map = {}
shuffled_list = list(character_range)
random.shuffle(shuffled_list)
for i, j in zip(list(character_range), shuffled_list):
    character_map[i] = j
with open("lab_exps/EXP02/cryptography/encryption/character_map.key", "w") as map:
    map.write(str(character_map))

print("Generated Character Map:", character_map)