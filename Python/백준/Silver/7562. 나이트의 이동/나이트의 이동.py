import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(x, y, l, gox, goy):
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        if x == gox and y == goy:
            return visited[y][x]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and visited[ny][nx] == 0:
                visited[ny][nx]  = visited[y][x] + 1
                q.append([nx, ny])

for _ in range(n):
    l = int(sys.stdin.readline().rstrip())
    nowLoca = list(map(int, sys.stdin.readline().rstrip().split()))
    goLoca = list(map(int, sys.stdin.readline().rstrip().split()))
    visited = [[0]*l for _ in range(l)]
    print(bfs(nowLoca[0], nowLoca[1], l, goLoca[0], goLoca[1]))