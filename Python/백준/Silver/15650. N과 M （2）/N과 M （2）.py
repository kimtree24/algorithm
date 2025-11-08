import sys
from itertools import combinations
input = sys.stdin.readline

n ,m = map(int,input().split(' '))

num_list = [num for num in range(1,n+1)]

num_set = combinations(num_list, m)

for each_set in num_set:
    print(*each_set)

