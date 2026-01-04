import sys
from collections import deque

input = sys.stdin.readline

# 전체 입력 받기
field = []
for i in range(12):
    line = list(input().strip())
    field.append(line)

# 상하좌우 이동 좌표
mov = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# 터뜨릴 것 탐색 (bfs)
def bfs(sr, sc, visit):
    q = deque()
    q.append((sr, sc))
    visit[sr][sc] = True
    color = field[sr][sc]
    group = [(sr, sc)]

    while q:
        cr, cc = q.popleft()
        for dr, dc in mov:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < 12 and 0 <= nc < 6:
                if not visit[nr][nc] and field[nr][nc] == color:
                    visit[nr][nc] = True
                    q.append((nr, nc))
                    group.append((nr, nc))
    return group


# 중력 반영
def down():
    for c in range(6):
        stack = []
        for r in range(12):
            if field[r][c] != '.':
                stack.append(field[r][c])
        for r in range(11, -1, -1):
            if stack:
                field[r][c] = stack.pop()
            else:
                field[r][c] = '.'

cnt = 0

while True:
    visit = [[False for _ in range(6)] for _ in range(12)]
    # 한번에 터질 것들 보관
    remove = []

    for r in range(12):
        for c in range(6):
            if field[r][c] != '.' and not visit[r][c]:
                group = bfs(r, c, visit)
                if len(group) >= 4:
                    remove.extend(group)
    if not remove:
        break

    for r, c in remove:
        field[r][c] = '.'
    down()
    cnt += 1
print(cnt)