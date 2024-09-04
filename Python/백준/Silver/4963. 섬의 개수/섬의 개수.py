import sys
from collections import deque

dx = [0, 0, -1, 1, -1, -1, 1, 1]  # x 방향
dy = [-1, 1, 0, 0, -1, 1, -1, 1]  # y 방향

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[y][x] = True

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx]:
                if graph[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((nx, ny))

while True:
    w, h = map(int, sys.stdin.readline().rstrip().split())
    if w == 0 and h == 0:
        break

    graph = []
    for i in range(h):
        line = list(map(int, sys.stdin.readline().rstrip().split()))
        graph.append(line)

    count = 0
    visited = [[False] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j] == 1:
                bfs(j, i)
                count += 1

    print(count)