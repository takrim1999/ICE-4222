def gcd(big,small):
    if small == 0:
        return big
    else:
        return gcd(small,big%small)

def phi(n):
    value = 0
    for i in range(n):
        if gcd(n,i) == 1:
            value += 1

    return value

print(phi(8))