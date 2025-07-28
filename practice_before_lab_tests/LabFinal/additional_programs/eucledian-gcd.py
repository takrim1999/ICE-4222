def gcd(big,small):
    if small == 0:
        return big
    else:
        return gcd(small,big%small)

print(gcd(12,18))