import sys
from collections import deque
input = sys.stdin.readline
t = int(input().strip())

for _ in range(t):
    p = input().strip()
    n = int(input().strip())
    arr = input().strip()
    
    if n == 0:
        dq = deque()
    else:
        dq = deque(map(int, arr[1:-1].split(',')))
    
    rev = False
    error = False

    for ch in p:
        if ch == 'R':
            rev = not rev
        else:
            if not dq:
                error = True
                break
            if not rev:
                dq.popleft()
            else:
                dq.pop()
    if error:
        print('error')
    else:
        if rev:
            dq.reverse()
        print('['+','.join(map(str,dq))+']')