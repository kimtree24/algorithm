from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    
    group_id = [[-1 for _ in range(m)] for _ in range(n)]
    group_size = []
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    
    gid = 0
    
    for r in range(n):
        for c in range(m):
            if land[r][c] == 1 and group_id[r][c] == -1:
                q = deque([(r, c)])
                group_id[r][c] = gid
                size = 1
                
                while q:
                    cr, cc = q.popleft()
                    for dr, dc in dirs:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < n and 0 <= nc < m:
                            if land[nr][nc] == 1 and group_id[nr][nc] == -1:
                                group_id[nr][nc] = gid
                                q.append((nr, nc))
                                size += 1
                group_size.append(size)
                gid += 1
    ans = 0
    for c in range(m):
        seen = set()
        total = 0
        for r in range(n):
            if group_id[r][c] != -1:
                seen.add(group_id[r][c])
        for g in seen:
            total += group_size[g]
        ans = max(ans, total)
    return ans