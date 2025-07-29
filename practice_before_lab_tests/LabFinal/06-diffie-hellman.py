from math import sqrt
import random
def is_primitive(a,b):
    root_set = set()
    for i in range(1,b):
        root_set.add((a**i) % b)
    if len(root_set) == b-1:
        return True
    return False

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

# step 1 Alice generates a huge prime number n and g(primitive root of n)
start_prime = 100
end_prime = 1000
n = random.randint(start_prime,end_prime)
while not is_prime(n):
    n = random.randint(start_prime, end_prime)
g = n-1
while not is_prime(g) and not is_primitive(n,g):
    g -= 1

# n = 37
# g = 13

# step 2 both takes a random number <= n-1 as their secret key
private_key_alice = random.randrange(n)
private_key_bob = random.randrange(n)

# step 3 alice calculates k1 = g^private_key_alice mod n and
# bob calculates k2 = g^private_key_bob mod n
# they shares k1 and k2 with each other

k1 = pow(g,private_key_alice,n)
k2 = pow(g,private_key_bob,n)

# step 4 alice calculates k2^private_key_alice mod n and
# bob calculates k1^private_key_bob mod n then the gets the same shared key.
print("Private key Alice: ", private_key_alice)
print("Private key Bob: ", private_key_bob)

shared_key_alice = pow(k2,private_key_alice,n)
shared_key_bob = pow(k1,private_key_bob,n)

print("Shared secret Alice: ", shared_key_alice)
print("Shared secret Bob: ", shared_key_bob)