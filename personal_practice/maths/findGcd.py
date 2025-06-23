def find(large,small):
    if small == 0:
        return abs(large)
    else:
        return find(small,large%small)

print(find(10,45))