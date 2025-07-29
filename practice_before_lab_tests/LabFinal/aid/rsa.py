def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd_val, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd_val, x, y


def generate_keys(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Give prime numbers: ")
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1
    , d, = extended_gcd(e, phi)
    d = d % phi
    return ((e, n), (d, n))


def encrypt(massage, public_key):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in massage]
    return cipher


def decrypt(cipher, privet_key):
    d, n = privet_key
    message = ''.join([chr(pow(char, d, n)) for char in cipher])
    return massage


p = int(input("Give the first prime number: "))
q = int(input("Give the Second prime number: "))
public_key, privet_key = generate_keys(p, q)

massage = input("Give a massage to encrypt: ")
encrypted = encrypt(massage, public_key)
decrypted = decrypt(encrypted, privet_key)

print("Public keys: ", public_key)
print("Pivet keys: ", privet_key)
print("Encrypted Massage: ", encrypted)
print("Decrypted Massage: ", decrypted)
