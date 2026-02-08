from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
dist = [-1] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])
visited[1] = True
dist[1] = 0

while q:
    x = q.popleft()
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            dist[nx] = dist[x] + 1
            q.append(nx)

ans = 0
for i in range(2, n + 1):
    if 1 <= dist[i] <= 2:
        ans += 1

print(ans)