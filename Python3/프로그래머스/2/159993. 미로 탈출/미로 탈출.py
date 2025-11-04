from collections import deque

def solution(maps):
    grid = [list(row) for row in maps]
    R, C = len(grid), len(grid[0])
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]

    # 좌표 찾기
    def find(ch):
        for r in range(R):
            for c in range(C):
                if grid[r][c] == ch:
                    return (r, c)
        return None

    S = find('S')
    L = find('L')
    E = find('E')
    if not S or not L or not E:
        return -1

    def bfs(start, target):
        sr, sc = start
        tr, tc = target
        dist = [[-1 for _ in range(C)] for _ in range(R)]
        q = deque([(sr, sc)])
        dist[sr][sc] = 0

        while q:
            r, c = q.popleft()
            if (r, c) == (tr, tc):
                return dist[r][c]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    if grid[nr][nc] != 'X' and dist[nr][nc] == -1:
                        dist[nr][nc] = dist[r][c] + 1
                        q.append((nr, nc))
        return -1

    d1 = bfs(S, L)
    if d1 == -1:
        return -1
    d2 = bfs(L, E)
    if d2 == -1:
        return -1
    return d1 + d2