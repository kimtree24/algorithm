import sys
import math
n = int(input())
s, m, l, xl, xxl, xxxl = map(int, sys.stdin.readline().rstrip().split())
t, p = map(int, sys.stdin.readline().rstrip().split())

listT = [s, m, l, xl, xxl, xxxl]
sum_T = 0
for i in listT:
    sum_T += (math.ceil(i/t))

print(sum_T)

print(n//p, n%p, sep = " ")