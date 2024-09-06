import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    if visited[y][x]:
        return visited[y][x]

    visited[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[y][x] < graph[ny][nx]:
            visited[y][x] = max(visited[y][x], dfs(nx, ny) + 1)
    return visited[y][x]

for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            dfs(x, y)

result = 0
for i in range(n):
    result = max(result, max(visited[i]))
print(result)