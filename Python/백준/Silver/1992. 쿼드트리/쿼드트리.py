import sys

input = sys.stdin.readline

n = int(input().strip())

# 전체 입력
matrix = []
for _ in range(n):
    line = list(map(int, input().strip()))
    matrix.append(line)

# 결과 stack
result = []

# 재귀함수
def trans(r, c, size):
    std = matrix[r][c]
    # 탈출조건
    flag = True  # 전부 같으면 true, 다른거 있으면 false
    for row in range(r, r + size):
        for col in range(c, c + size):
            if std != matrix[row][col]:
                flag = False
                break
        if not flag:
            break

    # 최종적으로 묶음 넣을지, 아니면 다음 depth로 넘어갈지 판단
    if flag:
        result.append(str(std))
        return
    else:
        result.append('(')
        n_size = size // 2
        trans(r, c, n_size)
        trans(r, c + n_size, n_size)
        trans(r + n_size, c, n_size)
        trans(r + n_size, c + n_size, n_size)
        result.append(')')
# 출력
trans(0,0,n)
print(''.join(result))