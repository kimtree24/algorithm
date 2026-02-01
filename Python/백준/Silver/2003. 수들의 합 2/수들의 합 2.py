import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))

left, right = 0,0
ans = 0
cur_sum = 0

while True:
    if cur_sum >= m:
        if cur_sum == m:
            ans += 1
        cur_sum -= nums[left]
        left += 1
    else:
        if right == n:
            break
        cur_sum += nums[right]
        right += 1
print(ans)
    