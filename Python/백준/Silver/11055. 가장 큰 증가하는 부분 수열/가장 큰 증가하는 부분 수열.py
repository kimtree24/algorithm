import sys

input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int, input().strip().split()))

max_sum_list = nums[:]

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            max_sum_list[i] = max(max_sum_list[i], max_sum_list[j] + nums[i])
print(max(max_sum_list))