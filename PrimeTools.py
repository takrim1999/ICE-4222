#!/usr/bin/python3

from OddEven import check_odd_even
from math import sqrt

def check_prime(n):
	if n == 1:
		return "not prime"
	if n == 2:
		return "prime"
	elif check_odd_even(n) == "even":
		return "not prime"
	else:
		i = 3
		flag = True
		while i<int(sqrt(n)):
			if n%i == 0:
				return "not prime"
		return "prime"



if __name__ == "__main__":
	num = int(input("Your number: "))
	print(check_prime(num))
