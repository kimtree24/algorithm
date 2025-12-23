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
    
    # 다음 숫자 탐색
    for i in range(start, n):
        result.append(nums[i])
        dfs(i + 1)
        result.pop()
dfs(0)