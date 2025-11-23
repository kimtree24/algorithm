import sys
input = sys.stdin.readline

n = int(input().strip())
stack = []
cnt = 0
result = []
cant = False
for i in range(n):
    cur = int(input().strip())
    flag = True
    if stack and cur < stack[-1]:
        cant = True
        break
    while flag:
        if cur >= cnt:
            cnt += 1
            stack.append(cnt)
            result.append('+')
        if stack[-1] == cur:
            stack.pop()
            result.append('-')
            flag = False
if cant:
    print('NO')
else:
    for i in result:
        print(i)