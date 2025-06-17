from math import sqrt
# start = 2
end = 10000
count = 0
for i in range(2,end+1):
    flag = True
    for j in range(2,round(sqrt(i))+1):
        if i%j==0:
            flag = False
    if flag:
        print(i, " is a prime!")
        count+=1
print(count)