import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())
nums = sorted(map(int, input().strip().split()))

visit = [False for _ in range(n)]
result = []

def dfs():
    # 탈출조건
    if len(result) == m:
        print(*result)
        return
    used = set()
    # 다음 레벨
    for i in range(n):
        if nums[i] not in used and not visit[i]:
            used.add(nums[i])
            visit[i] = True
            result.append(nums[i])
            dfs()
            result.pop()
            visit[i] = False
dfs()