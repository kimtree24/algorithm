import sys
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int, input().strip().split()))

sum_len_list = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            sum_len_list[i] = max(sum_len_list[i], sum_len_list[j] + 1)
print(max(sum_len_list))