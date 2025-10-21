from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])  # 세로, 가로
    # 4방향 (상,하,좌,우)
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    visit = [[0]*m for _ in range(n)]
    visit[0][0] = 1
    
    q = deque([(0,0)])
    while q:
        y, x = q.popleft()
        # 목표 지점 도달하면 바로 반환
        if y == n-1 and x == m-1:
            return visit[y][x]
        
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if maps[ny][nx] == 1 and visit[ny][nx] == 0:  # 길이고 미방문
                    visit[ny][nx] = visit[y][x] + 1
                    q.append((ny, nx))
    
    # 도달 불가
    return -1