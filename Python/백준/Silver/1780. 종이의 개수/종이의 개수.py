import sys

input = sys.stdin.readline

n = int(input().strip())

# 최초 종이 입력
first_matrix = []
for _ in range(n):
    line = list(map(int,input().strip().split()))
    first_matrix.append(line)

# 결과 카운트
cnt = [0,0,0]

def cut_paper(r, c, size):
    std = first_matrix[r][c]
    flag = True

    for row in range(r, r + size):
        for col in range(c, c + size):
            if first_matrix[row][col] != std:
                flag = False
                break
        if not flag:
            break

    if flag:
        cnt[std + 1] += 1
        return

    new_size = size // 3
    for row in range(3):
        for col in range(3):
            cut_paper(r + row * new_size, c + col * new_size, new_size)
cut_paper(0,0,n)
print(cnt[0])
print(cnt[1])
print(cnt[2])