from collections import deque

n = int(input())

graph = [[] for _ in range(n + 1)]
while True:
    line = list(map(int, input().strip().strip().split()))
    a, b = line[0], line[1]
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

sc = [0 for _ in range(n + 1)]

for start in range(1, n + 1):
    visited = [-1 for _ in range(n + 1)]
    q = deque([start])
    visited[start] = 0

    while q:
        x = q.popleft()
        for nx in graph[x]:
            if visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[x] + 1
    sc[start] = max(visited[1:])
min_sc = min(sc[1:])

result = []
for i in range(1, n + 1):
    if sc[i] == min_sc:
        result.append(i)
print(min_sc, len(result))
print(*result)

