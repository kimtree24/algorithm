import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().strip().split())

# 지도 초기화
matrix = []
for _ in range(n):
    row = list(map(int, input().strip().split()))
    matrix.append(row)
# 주사위 초기화
dice = {"top": 0, "east": 0, "west": 0, "bottom": 0, "north": 0, "south": 0}
# 현재 주사위 위치
cur = [x,y]

# 이동 함수
def move(cmd):
    x,y = cur
    # 동
    if cmd == 1:
        if y + 1 >= m:
            return
        cur[1] += 1

        temp = dice["top"]
        dice["top"] = dice["west"]
        dice["west"] = dice["bottom"]
        dice["bottom"] = dice["east"]
        dice["east"] = temp

    # 서
    elif cmd == 2:
        if y - 1 < 0:
            return
        cur[1] -= 1

        temp = dice["top"]
        dice["top"] = dice["east"]
        dice["east"] = dice["bottom"]
        dice["bottom"] = dice["west"]
        dice["west"] = temp

    # 북
    elif cmd == 3:
        if x - 1 < 0:
            return
        cur[0] -= 1

        temp = dice["top"]
        dice["top"] = dice["south"]
        dice["south"] = dice["bottom"]
        dice["bottom"] = dice["north"]
        dice["north"] = temp

    # 남
    elif cmd == 4:
        if x + 1 >= n:
            return
        cur[0] += 1

        temp = dice["top"]
        dice["top"] = dice["north"]
        dice["north"] = dice["bottom"]
        dice["bottom"] = dice["south"]
        dice["south"] = temp

    # 바닥 ↔ 지도 복사
    x, y = cur
    if matrix[x][y] == 0:
        matrix[x][y] = dice["bottom"]
    else:
        dice["bottom"] = matrix[x][y]
        matrix[x][y] = 0

    print(dice["top"])


# 명령 실행
commands = list(map(int, input().split()))
for cmd in commands:
    move(cmd)
