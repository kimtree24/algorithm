import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().strip().split())
nums = sorted(list(map(int, input().strip().split())))

permu = list(permutations(nums, m))

for each in permu:
    print(*each)