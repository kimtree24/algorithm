from collections import deque
import copy
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    queue = deque()
    temp_graph = copy.deepcopy(graph)

    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if temp_graph[nx][ny] == 0:
                    temp_graph[nx][ny] = 2
                    queue.append((nx,ny))
    global answer
    safeZone = 0

    for i in range(n):
        safeZone += temp_graph[i].count(0)

    answer = max(answer, safeZone)

def makeWall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                graph[i][j] = 0

answer = 0
makeWall(0)
print(answer)