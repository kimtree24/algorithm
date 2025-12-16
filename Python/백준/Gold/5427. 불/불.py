import sys
from collections import deque
input = sys.stdin.readline

t = int(input().strip())

# 좌표이동 상하좌우
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

for _ in range(t):
    c, r = map(int,input().split())

    bld = []
    fire_q = deque()
    man_q = deque()
    
    fire_time = [[-1 for _ in range(c)] for _ in range(r)]
    man_time = [[-1 for _ in range(c)] for _ in range(r)]
    
    for row in range(r):
        line = list(input().strip())
        bld.append(line)
        for col in range(c):
            if line[col] == '*':
                fire_q.append((row, col))
                fire_time[row][col] = 0
            elif line[col] == '@':
                man_q.append((row, col))
                man_time[row][col] = 0
    
    while fire_q:
        cr, cc = fire_q.popleft()
        for dr, dc in dirs:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < r and 0 <= nc < c:
                if fire_time[nr][nc] == -1 and bld[nr][nc] == '.':
                    fire_time[nr][nc] = fire_time[cr][cc] + 1
                    fire_q.append((nr,nc))
    
    flag = False
    while man_q:
        cr, cc = man_q.popleft()
        
        # 탈출조건
        if cr == 0 or cr == r-1 or cc == 0 or cc == c-1:
            print(man_time[cr][cc] + 1)
            flag = True
            break
            
        for dr, dc in dirs:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < r and 0 <= nc < c:
                if bld[nr][nc] == '.' and man_time[nr][nc] == -1:
                    if fire_time[nr][nc] == -1 or fire_time[nr][nc] > man_time[cr][cc] + 1:
                        man_time[nr][nc] = man_time[cr][cc] + 1
                        man_q.append((nr, nc))
    
    if not flag:
        print("IMPOSSIBLE")
            