import sys
from collections import deque

input = sys.stdin.readline


gears = [None]
for _ in range(4):
    gears.append(deque(map(int, input().strip())))

k = int(input())

for _ in range(k):
    n, r = map(int, input().split())

    rotate = [0] * 5
    rotate[n] = r

    # 왼쪽
    for i in range(n, 1, -1):
        if gears[i][6] != gears[i - 1][2]:
            rotate[i - 1] = -rotate[i]
        else:
            break

    # 오른쪽
    for i in range(n, 4):
        if gears[i][2] != gears[i + 1][6]:
            rotate[i + 1] = -rotate[i]
        else:
            break

    # 회전 적용
    for i in range(1, 5):
        if rotate[i] != 0:
            gears[i].rotate(rotate[i])

score = 0
if gears[1][0] == 1:
    score += 1
if gears[2][0] == 1:
    score += 2
if gears[3][0] == 1:
    score += 4
if gears[4][0] == 1:
    score += 8

print(score)