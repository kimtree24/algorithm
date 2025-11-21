import sys
import bisect

input = sys.stdin.readline

n = int(input().strip())
num_list = sorted(list(map(int, input().strip().split())))
x = int(input().strip())

cnt = 0

for i in range(n):
    target = x - num_list[i]
    idx = bisect.bisect_left(num_list, target, i + 1)
    if idx < n and num_list[idx] == target:
        cnt += 1
print(cnt)