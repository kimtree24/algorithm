import sys
input = sys.stdin.readline

line = list(input().strip())
stack = []
ans = 0

for i, ch in enumerate(line):
    if ch == '(':
        stack.append(ch)
    else:
        stack.pop()
        #레이저
        if line[i-1] == "(":
            ans += len(stack)
        else:
            ans += 1
print(ans)