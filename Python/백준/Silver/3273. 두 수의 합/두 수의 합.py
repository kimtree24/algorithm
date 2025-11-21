import sys

input = sys.stdin.readline

n = int(input().strip())
num_list = sorted(list(map(int, input().strip().split())))
x = int(input().strip())
cnt = 0

left, right = 0, n - 1
while left < right:
    s = num_list[left] + num_list[right]
    if s == x:
        cnt += 1
        left += 1
        right -= 1
    elif s < x:
        left += 1
    else:
        right -= 1

print(cnt)