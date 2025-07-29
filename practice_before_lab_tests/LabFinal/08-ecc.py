# Elliptic curve over a finite field: y² = x³ + ax + b (mod p)
class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def is_on_curve(self, P):
        if P is None: return True
        x, y = P
        return (y*y - x*x*x - self.a*x - self.b) % self.p == 0

    def point_add(self, P, Q):
        if P is None: return Q
        if Q is None: return P
        x1, y1 = P
        x2, y2 = Q
        if x1 == x2 and y1 != y2:
            return None
        if P == Q:
            l = (3 * x1 * x1 + self.a) * pow(2 * y1, -1, self.p)
        else:
            l = (y2 - y1) * pow(x2 - x1, -1, self.p)
        l %= self.p
        x3 = (l * l - x1 - x2) % self.p
        y3 = (l * (x1 - x3) - y1) % self.p
        return (x3, y3)

    def scalar_mult(self, k, P):
        result = None
        while k > 0:
            if k % 2 == 1:
                result = self.point_add(result, P)
            P = self.point_add(P, P)
            k //= 2
        return result


# Use small toy curve: y² = x³ + 2x + 2 over F_17
curve = EllipticCurve(a=2, b=2, p=17)
G = (5, 1)  # base point
assert curve.is_on_curve(G)

# Alice generates private key (random scalar)
alice_priv = 5
alice_pub = curve.scalar_mult(alice_priv, G)

# Bob generates private key
bob_priv = 7
bob_pub = curve.scalar_mult(bob_priv, G)

# Shared secret (both should compute the same point)
shared_alice = curve.scalar_mult(alice_priv, bob_pub)
shared_bob = curve.scalar_mult(bob_priv, alice_pub)

print("Alice Shared Point:", shared_alice)
print("Bob Shared Point:  ", shared_bob)

def simple_key_from_point(P):
    x, y = P
    return x ^ y  # very basic "key" for demonstration

def xor_encrypt(message: str, key: int):
    return bytes([ord(c) ^ key for c in message])

def xor_decrypt(cipher: bytes, key: int):
    return ''.join([chr(b ^ key) for b in cipher])

# Simulate Alice encrypting a message for Bob
shared_secret = shared_alice
key = simple_key_from_point(shared_secret)

plaintext = "ECC is cool!"
cipher = xor_encrypt(plaintext, key)
decrypted = xor_decrypt(cipher, key)

print("Ciphertext:", cipher)
print("Decrypted:", decrypted)
