# Step 1 is to generate 2 pseudo random numbers p and q
import random
from math import sqrt

prime_start = 250
prime_end = 500

def gcd(large, small):
    if small == 0:
        return large
    else:
        return gcd(small,large%small)

def egcd(small, large):
    if small == 0:
        return large, 0, 1
    else:
        gcd, x1, y1 = egcd(large%small, small)
        x = y1 - (large//small) * x1
        y = x1
        return gcd, x, y

def is_prime(number):
    if number in [0,1]:
        return False
    if number in [2,3]:
        return True
    if number&1==0:
        return False
    for i in range(3,int(sqrt(number))+1):
        if number%i==0:
            return False
    return True

p = random.randint(prime_start,prime_end)
q = random.randint(prime_start,prime_end)

while not is_prime(p):
    p = random.randint(prime_start, prime_end)
while not is_prime(q):
    q = random.randint(prime_start, prime_end)

# step 2 is to calculate phi(n) where n = p * q
# but generic method to calculate phi(n) is to find from 1 to n-1 how many are gcd(iterable,n) == 1
# we can simply do it by (p-1)*(q-1), so phi(p,q) = (p-1)*(q-1)
n = p*q # this is needed to calculate the keys
phi = (p-1)*(q-1)

# step 3 is to calculate a public key e as gcd(e,phi(n)) = 1
e = random.randrange(1,phi)
while gcd(phi,e) != 1:
    e = random.randrange(1, phi)

# step 4 is to calculate a private key d as d * e mod phi = 1
# that means we need to find the modular multiplicative inverse of e
if e<phi:
    d = egcd(e,phi)[1]
else:
    d = egcd(phi, e)[1]

print("public key: ", (d,n))
print("private key: ", (e,n))

def encrypt(plain_text, public_key):
    cipher = ""
    d , n = public_key
    for char in plain_text:
        cipher += chr(pow(ord(char),d,n))
    return cipher

def decrypt(cipher_text, private_key):
    text = ""
    e, n = private_key
    for char in cipher_text:
        text += chr(pow(ord(char),e,n))
    return text

plain_text = "Hello, World!"
public_key = (d,n)
private_key = (e,n)
cipher_text = encrypt(plain_text, public_key)
recovered_text = decrypt(cipher_text, private_key)
print("Text: ", plain_text)
print("Cipher: ", cipher_text)
print("Recovered Text: ", recovered_text)