import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())

q = deque()
for _ in range(n):
    line = list(sys.stdin.readline().rstrip().split())
    num = 0
    if line[0] == 'push':
        num = int(line[1])
        q.append(num)
    elif line[0] == 'pop':
        if len(q) != 0:
            print(q.popleft())
        else:
            print(-1)
    elif line[0] == 'size':
        print(len(q))
    elif line[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif line[0] == 'front':
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
    elif line[0] == 'back':
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)
        
        