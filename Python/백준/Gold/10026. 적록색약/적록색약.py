import sys
from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

n = int(sys.stdin.readline().rstrip())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
    
count = 0

def bfs(x, y):
    q = deque()
    q.append([x,y])
    visited[x][y] = True
    color = graph[x][y]
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append([nx, ny])

count1 = 0
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count1 += 1
            
count2 = 0
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
            
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count2 += 1
print(count1, count2)