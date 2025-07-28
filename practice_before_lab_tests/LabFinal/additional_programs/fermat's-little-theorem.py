# First we need to take a prime p and any positive integer a not divisible by p
# First we need to check a number is prime or not.
from math import sqrt
import random

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

p = random.randint(2,100)
while not is_prime(p):
    p = random.randint(2,100)
a = random.randint(2,100)
while a%p==0:
    a = random.randint(2,100)
print("p: ", p)
print("a: ", a)
print("p-1: ", p-1)
print("a^p-1: ",pow(a,(p-1)))
print("a^p-1 mod p(should be 1): ", pow(a,(p-1))%p)