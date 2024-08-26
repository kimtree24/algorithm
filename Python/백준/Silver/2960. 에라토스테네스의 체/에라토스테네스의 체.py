import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
numList = [i for i in range(2,n+1)]
result = 0
count = 0
while len(numList) != 0 and count < k:
    temp = numList[0]
    i = 1
    while temp*i <= n and count < k:
        if temp*i in numList:
            numList.remove(temp*i)
            result = temp * i
            i +=1
            count +=1
        else:
            i+=1
print(result)