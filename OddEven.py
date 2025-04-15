#!/usr/bin/python3

"""
Checks wheather your number is odd or even
you can import from odd-even check_odd_even
and test it
"""

def check_odd_even(n):
    if n&1==0:
        return "even"
    else:
        return "odd"



if  __name__ == "__main__":
	num = int(input("Input you number: "))
	print(check_odd_even(num))

