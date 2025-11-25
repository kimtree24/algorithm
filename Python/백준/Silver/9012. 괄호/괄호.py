import sys

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    stack = []
    line = list(input().strip())
    for ch in line:
        if stack and ch == '(':
            stack.append(ch)
        elif stack and ch == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(ch)
        else:
            stack.append(ch)
    if stack:
        print('NO')
    else:
        print('YES')