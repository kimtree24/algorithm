import sys
input = sys.stdin.readline

n, m = map(int,input().strip().split())
nums = sorted(list(map(int, input().strip().split())))

result = []

def dfs():
    # 탈출조건
    if len(result) == m:
        print(*result)
        return
    # 다음판단
    for i in range(n):
        result.append(nums[i])
        dfs()
        result.pop()
dfs()