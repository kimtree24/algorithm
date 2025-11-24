import sys
from collections import deque

input = sys.stdin.readline


def instruction(q, ins):
    ins_set = ins.split()
    if ins_set[0] == 'push':
        q.append(int(ins_set[1]))
    elif ins_set[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif ins_set[0] == 'size':
        print(len(q))
    elif ins_set[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif ins_set[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif ins_set[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])


n = int(input().strip())
q = deque([])
for i in range(n):
    ins = input().strip()
    instruction(q, ins)