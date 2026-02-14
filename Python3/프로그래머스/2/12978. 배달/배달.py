import heapq

def solution(N, road, K):
    
    graph = [[] for _ in range(N + 1)]
    
    for each_road in road:
        a, b, w = each_road
        graph[a].append((b, w))
        graph[b].append((a, w))
    
    dist = [float('inf') for _ in range(N + 1)]
    dist[1] = 0
    
    q = []
    heapq.heappush(q, (1, 0))
    
    while q:
        node, cur_dist = heapq.heappop(q)
        
        if cur_dist > dist[node]:
            continue
        
        for nx, w in graph[node]:
            nd = cur_dist + w
            if nd < dist[nx]:
                dist[nx] = nd
                heapq.heappush(q, (nx, nd))
    ans = 0
    for d in dist:
        if d <= K:
            ans += 1
    return ans