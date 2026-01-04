import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())
nums = sorted(map(int, input().strip().split()))

result = []

def dfs():
    if len(result) == m:
        print(*result)
        return
    used = set()
    for i in range(n):
        if nums[i] not in used:
            used.add(nums[i])
            result.append(nums[i])
            dfs()
            result.pop()
dfs()