import sys
n = int(sys.stdin.readline().rstrip())
matrix = []
for i in range(n):
    line = sys.stdin.readline().rstrip()
    matrix.append(list(line))

def sol(matrix):
    max_count = 1
    for i in range(n):
        count = 1
        for j in range(1, n):
            if matrix[i][j] == matrix[i][j-1]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)
    for j in range(n):
        count = 1
        for i in range(1, n):
            if matrix[i][j] == matrix[i-1][j]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)
    return max_count

maxResult = sol(matrix)

for i in range(n):
    for j in range(n):
        if i + 1 < n:
            matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
            maxResult = max(maxResult, sol(matrix))
            matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
        if j + 1 < n:
            matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
            maxResult = max(maxResult, sol(matrix))
            matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
print(maxResult)