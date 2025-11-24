import sys
from collections import deque

input = sys.stdin.readline
n = int(input().strip())
q = deque([i for i in range(1, n+1)])

while len(q) > 0:
    if len(q) == 1:
        print(q.popleft())
        break
    else:
        q.popleft()
        temp = q.popleft()
        q.append(temp)