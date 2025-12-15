import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())

matrix = []
q = deque()

for z in range(h):
    layer = []
    for r in range(n):
        row = list(map(int, input().split()))
        layer.append(row)
        for c, v in enumerate(row):
            if v == 1:
                q.append((z, r, c))
    matrix.append(layer)

dir = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

while q:
    z, r, c = q.popleft()
    for dz, dr, dc in dir:
        nz, nr, nc = z + dz, r + dr, c + dc
        if 0 <= nz < h and 0 <= nr < n and 0 <= nc < m:
            if matrix[nz][nr][nc] == 0:
                matrix[nz][nr][nc] = matrix[z][r][c] + 1
                q.append((nz, nr, nc))

ans = 0
flag = False
for z in range(h):
    for r in range(n):
        for c in range(m):
            if matrix[z][r][c] == 0:
                flag = True
            ans = max(ans, matrix[z][r][c])
if flag:
    print(-1)
else:
    print(ans - 1)