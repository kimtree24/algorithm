import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())
nums = sorted(map(int, input().strip().split()))

result = []

def dfs(start):
    # 탈출조건
    if len(result) == m:
        print(*result)
        return
    # 다음 레벨
    used = set()  # 지금 레벨에서 사용되었는지 여부
    for i in range(start, n):
        if nums[i] not in used:
            used.add(nums[i])
            result.append(nums[i])
            dfs(i + 1)
            result.pop()

dfs(0)