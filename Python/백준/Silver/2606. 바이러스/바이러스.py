n = int(input().strip())
m = int(input().strip())

graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    visited[x] = True
    for nx in graph[x]:
        if not visited[nx]:
            dfs(nx)

dfs(1)

print(sum(visited) - 1)