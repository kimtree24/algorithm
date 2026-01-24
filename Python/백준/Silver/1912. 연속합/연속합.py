import sys
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int, input().strip().split()))

cur = nums[0]
ans = nums[0]

for i in range(1, n):
    cur = max(nums[i], cur + nums[i])
    ans = max(ans, cur)
print(ans)