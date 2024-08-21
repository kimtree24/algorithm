import sys

n = int(input())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))

num_list.sort()

start = 0
end = n - 1
ref = num_list[start] + num_list[end]
ans_start = num_list[start]
ans_end = num_list[end]

while start < end:

    if abs(num_list[start] + num_list[end]) < abs(ref):
        ans_start = num_list[start]
        ans_end = num_list[end]
        ref = num_list[start] + num_list[end]
    elif abs(num_list[start] + num_list[end]) == 0:
        ans_start = num_list[start]
        ans_end = num_list[end]
        break

    if num_list[start] + num_list[end] >= 0:
        end -= 1
    else:
        start += 1


print(ans_start, ans_end)