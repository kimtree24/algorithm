from collections import defaultdict

def solution(n, wires):
    graph = defaultdict(list)
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    parent = [0] * (n + 1)
    subtree = [0] * (n + 1)

    def dfs(u, p):
        parent[u] = p
        size = 1
        for v in graph[u]:
            if v == p:
                continue
            size += dfs(v, u)
        subtree[u] = size
        return size

    dfs(1, 0)
    ans = n
    for a, b in wires:
        if parent[b] == a:
            size = subtree[b]
        elif parent[a] == b:
            size = subtree[a]
        else:
            continue
        diff = abs(n - 2 * size)
        if diff < ans:
            ans = diff

    return ans