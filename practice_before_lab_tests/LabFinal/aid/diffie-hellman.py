import random


def findPrimitiveRoot(p):
    roots = []
    for q in range(2, p):
        results = []
        for i in range(1, p):
            r = pow(q, i, p)
            if r in results:
                break
            else:
                results.append(r)
        if len(results) == p - 1:
            roots.append(q)
    return roots


p = int(input("Enter Prime Number(P): "))
roots = findPrimitiveRoot(p)

print(f"Select a primitive root of {p} is {roots}")
g = 0
while (True):
    g = int(input("Select a number from the above list: "))
    if (g in roots):
        break
    print(f"{g} is not a primitive root of {p}. Try again")

# Key for A
Xa = random.randint(2, p - 1)
Ya = g ** Xa % p

# Key for B
Xb = random.randint(2, p - 1)
while (Xb == Xa):
    Xb = random.randint(2, p - 1)

Yb = g ** Xb % p

# Shared key for A & B
Ka = Yb ** Xa % p
Kb = Ya ** Xb % p

print(f"Secret for A: {Xa}")
print(f"Public for A: {Ya}")

print(f"Secret for B: {Xb}")
print(f"Public for B: {Yb}")

print(f"Shared key for A: {Ka}")
print(f"Shared key for B: {Kb}")