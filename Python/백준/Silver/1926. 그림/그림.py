import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, sys.stdin.readline().rstrip().split())
visited = [[False] * m for _ in range(n)]
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

count = 0
max_size = 0

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[y][x] = True
    size = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and graph[ny][nx] == 1:
                q.append([nx, ny])
                visited[ny][nx] = True
                size += 1
    return size

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            count += 1
            max_size = max(max_size, bfs(j, i))
            
print(count)
print(max_size)
