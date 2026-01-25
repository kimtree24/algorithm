import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    p = [1 for _ in range(n)]
    for i in range(3, n):
        p[i] = p[i - 3] + p[i - 2]
    print(p[n - 1])