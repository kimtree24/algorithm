import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
nums = sorted(map(int, input().strip().split()))

result = []

def dfs(start):
    # 탈출여부
    if len(result) == m:
        print(*result)
        return
    # 다음레벨
    for i in range(start, n):
        result.append(nums[i])
        dfs(i)
        result.pop()
dfs(0)