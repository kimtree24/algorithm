import sys
input = sys.stdin.readline

n = int(input().strip())

matrix = [0 for _ in range(n + 1)]

matrix[1] = 1
if n >= 2:
    matrix[2] = 1

if n >= 3:
    for i in range(3, n + 1):
        matrix[i] = matrix[i - 2] + matrix[i - 1]
print(matrix[-1])