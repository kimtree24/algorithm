import sys
input = sys.stdin.readline

n = int(input().strip())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().strip().split())))

result = 0
index = 0

for row in range(1, n):
    for col in range(len(matrix[row])):
        if col == 0:
            matrix[row][col] += matrix[row - 1][0]
        elif col == row:
            matrix[row][col] += matrix[row - 1][col - 1]
        else:
            matrix[row][col] += max(matrix[row - 1][col - 1], matrix[row - 1][col])
print(max(matrix[n - 1]))