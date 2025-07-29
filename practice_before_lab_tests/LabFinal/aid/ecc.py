# Elliptic Curve Cryptography

p = int(input("Enter a Prime number,p: "))
a = int(input("Enter a coefficient a: "))
b = int(input("Enter a coefficient b: "))


def points_on_curve(a, b):
    affine_points = []
    n = 0
    for x in range(p):
        rhs = (x ** 3 + a * x + b) % p
        for y in range(p):
            if (y * y) % p == rhs:
                affine_points.append((x, y))
                n += 1
    return affine_points, n


print("affine points: ", points_on_curve(a, b))


def point_doubling(G):
    if G is None:
        return None

    x1, y1 = G

    if y1 == 0:
        return None

    s = (3 * x1 * x1 + a) * pow(2 * y1, -1, p) % p
    x3 = (s * s - 2 * x1) % p
    y3 = (s * (x1 - x3) - y1) % p

    return (x3, y3)


def point_addition(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2:
        if y1 != y2 or y1 == 0:
            return None

    if P == Q:
        return point_doubling(P)

    s = (y2 - y1) * pow(x2 - x1, -1, p) % p
    x3 = (s * s - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p
    return (x3, y3)


# Generator point input
# Gx = int(input("Enter x of generator point G: "))
# Gy = int(input("Enter y of generator point G: "))
# G = (Gx, Gy)

# print("1G = ",(G))

# print("2G = ", point_doubling(G))


def order_of_G(G):
    Q = G
    order = 1
    points_order = []
    print(f"{order}G: ", (Q))
    points_order.append(Q)
    while True:
        Q = point_addition(Q, G)
        order += 1

        if Q is None:
            print(f"{order}G: Identity (∞)")
            break

        print(f"{order}G: ", (Q))
        points_order.append(Q)
    return order, points_order


# n,points_order = order_of_G(G)
# print(n,points_order)

def max_order():
    affine_points, _ = points_on_curve(a, b)
    max_G = 0
    generatorPoint = None
    points_of_G_order = []

    for point in affine_points:
        print("Generator point: ", point)
        n, points = order_of_G(point)

        if n > max_G:
            generatorPoint = point
            points_of_G_order = points
            max_G = n

    return max_G, generatorPoint, points_of_G_order


# print("Order of Affine",max_order())

max_G, generatorPoint, points_of_G_order = max_order()

print(f"max_G: {max_G} \ngeneratorPoint: {generatorPoint}\n points_of_G_order: {points_of_G_order}")

# Key exchange Using ECC

# Private key of Bob 1<= B <= n-1

B = int(input("Enter a private key of Bob B: "))
A = int(input("Enter a private key of Alice A: "))

# Compute Public Key of Bob Pb = BG and Alice Pa = AG

Pb = points_of_G_order[B - 1]
Pa = points_of_G_order[A - 1]

print(Pa, Pb)

# Computes Bob's key
key_order1, key_points1 = order_of_G(Pa)

Kb = key_points1[B - 1]
print("Bob's key", Kb)

# Computes Alice's key
key_order2, key_points2 = order_of_G(Pb)

Ka = key_points2[A - 1]
print("Alice key", Ka)

# Encryption of ECC Cm = {AG , Pm + Ka}

P = (6, 3)  # Plaintext

Cm = (Pa, point_addition(P, Ka))  # Cipher text

# Decryption of ECC Pm = P + Ka - Kb
Pmx = P[0] + Ka[0] - Kb[0]
Pmy = P[1] + Ka[1] - Kb[1]

Pm = (Pmx, Pmy)

print("Cipher text and plaintext", Cm, Pm)