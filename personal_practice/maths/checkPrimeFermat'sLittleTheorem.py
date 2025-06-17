end = 10000

count = 0
def check_prime(num):
    global count
    if 5**(num-1)%num==1:
        print(num, " is prime!")
        count += 1

for i in range(2,end+1):
    check_prime(i)
print(count)