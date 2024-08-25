import sys
import math
m, n = map(int, sys.stdin.readline().rstrip().split())
lis =[i for i in range(m,n+1)]
for i in lis:
    count = True
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            count = False
            break
    if i == 1:
        count = False
    if count:
        print(i)