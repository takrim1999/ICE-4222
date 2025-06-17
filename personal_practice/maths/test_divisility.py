numlist = list(range(10001))
for i in range(2,10001):
    if numlist[i]%numlist[i-1] == 0:
        print(numlist[i], numlist[i-1])