import sys
input = sys.stdin.readline

n = int(input().strip())

t_list = []
p_list = []

for _ in range(n):
    t, p = map(int, input().strip().split())
    t_list.append(t)
    p_list.append(p)

dp = [0 for _ in range(n + 1)]

for i in range(n - 1, -1, -1):
    if i + t_list[i] <= n:
        dp[i] = max(dp[i+1], p_list[i] + dp[i + t_list[i]]) 
    else:
        dp[i] = dp[i + 1]
print(dp[0])