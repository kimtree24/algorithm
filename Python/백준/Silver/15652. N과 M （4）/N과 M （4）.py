import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

# 숫자 리스트 만들기
nums = [i for i in range(1, n + 1)]

result = []

def dfs(start):
    # 탈출조건
    if len(result) == m:
        print(*result)
        return
    for i in range(start, n + 1):
        result.append(i)
        dfs(i)
        result.pop()
dfs(1)
