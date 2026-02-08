import sys
from collections import defaultdict

input = sys.stdin.readline

k, l = map(int, input().strip().split())
st_dict = defaultdict(int)
for i in range(l):
    st_num = input().strip()
    st_dict[st_num] = i

sorted_st = sorted(st_dict.items(), key = lambda x:x[1])

for st_num, i in sorted_st[:k]:
    print(st_num)