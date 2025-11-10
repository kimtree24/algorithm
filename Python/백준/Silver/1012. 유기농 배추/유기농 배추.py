from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    r, c, k = map(int, input().split())
    # 배추 좌표 만들기
    grid = [[0 for _ in range(c)] for _ in range(r)]
    for _ in range(k):
        e_r, e_c = map(int, input().split())
        grid[e_r][e_c] = 1
    
    # 방문여부
    visit = [[False for _ in range(c)] for _ in range(r)]
    # 상하좌우
    di = [(-1,0), (1,0), (0,-1), (0,1)]
    ans = 0
    # bfs 탐색
    def bfs(sr, sc):
        q = deque()
        q.append((sr,sc))
        visit[sr][sc] = True
        while q:
            cr, cc = q.popleft()
            for dr, dc in di:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < r and 0 <= nc < c:
                    if not visit[nr][nc] and grid[nr][nc] == 1:
                        visit[nr][nc] = True
                        q.append((nr, nc))
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1 and not visit[i][j]:
                bfs(i, j)
                ans += 1
    print(ans)