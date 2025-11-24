import sys
from collections import deque

n, m = map(int, input().strip().split())

idx_list = list(map(int, input().strip().split()))

cnt = 0
q = deque(range(1, n+1))

for idx in idx_list:
    cur_idx = q.index(idx)
    
    if cur_idx <= len(q) // 2:
        q.rotate(-cur_idx)
        cnt += cur_idx
    else:
        r = len(q) - cur_idx
        q.rotate(r)
        cnt += r
    q.popleft()
print(cnt)