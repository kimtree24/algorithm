import sys
input = sys.stdin.readline

n,m = map(int, input().strip().split())
nums = sorted(map(int, input().strip().split()))

result = []

def dfs(start):
    if len(result) == m:
        print(*result)
        return
    used = set()
    for i in range(start,n):
        if nums[i] not in used:
            used.add(nums[i])
            result.append(nums[i])
            dfs(i)
            result.pop()
dfs(0)