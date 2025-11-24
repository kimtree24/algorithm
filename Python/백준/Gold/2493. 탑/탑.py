import sys
input = sys.stdin.readline

n = int(input().strip())

stack = []
height = list(map(int, input().split()))
answer = [0 for _ in range(n)]

for i, h in enumerate(height):
    while stack and stack[-1][0] < h:
        stack.pop()
    if stack:
        answer[i] = stack[-1][1] + 1
    stack.append((h, i))
print(*answer)
