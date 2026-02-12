from collections import deque
n = int(input())

graph = [list(map(int,(input().strip().split()))) for _ in range(n)]

for start in range(n):
    visited = [False for _ in range(n)]
    q = deque([start])

    while q:
        x = q.popleft()
        for nx in range(n):
            if graph[x][nx] and not visited[nx]:
                visited[nx] = True
                q.append(nx)
    for j in range(n):
        if visited[j]:
            graph[start][j] = 1
for row in graph:
    print(*row)
