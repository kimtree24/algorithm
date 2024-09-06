import sys

n = int(sys.stdin.readline().rstrip())
a, b = map(int, sys.stdin.readline().rstrip().split())
num = int(sys.stdin.readline().rstrip())
family = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = -1

for _ in range(num):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    family[x].append(y)
    family[y].append(x)

def dfs(v, count):
    visited[v] = True
    global result

    if v == b:
        result = count
        return

    for i in family[v]:
        if not visited[i]:
            dfs(i, count + 1)

dfs(a, 0)
print(result)