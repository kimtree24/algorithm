import sys
input = sys.stdin.readline

line = list(input().strip())

def solution(line):
    stack = []
    value = []
    
    for ch in line:
        if ch in '([':
            stack.append(ch)
            value.append(0)
        elif ch == ")":
            if not stack or stack[-1] != '(':
                return 0
            stack.pop()
            
            v = value.pop()
            if v == 0:
                v = 2
            else:
                v *= 2
            if value:
                value[-1] += v
            else:
                value.append(v)
        elif ch == "]":
            if not stack or stack[-1] != '[':
                return 0
            stack.pop()
            
            v = value.pop()
            if v == 0:
                v = 3
            else:
                v *= 3
            if value:
                value[-1] += v
            else:
                value.append(v)
    if stack:
        return 0
    return value.pop()

ans = solution(line)
print(ans)