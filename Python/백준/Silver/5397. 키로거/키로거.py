from collections import deque
import sys

input = sys.stdin.readline

t = int(input().strip())

# 커서 오른쪽 이동
def go_right(l_q, r_q):
    tmp = r_q.popleft()
    l_q.append(tmp)

# 커서 왼쪽 이동
def go_left(l_q, r_q):
    tmp = l_q.pop()
    r_q.appendleft(tmp)

# 삭제 동작
def del_chr(l_q):
    l_q.pop()

for test in range(t):
    l_q = deque()
    r_q = deque()
    line = list(input().strip())
    for ch in line:
        # 커서 왼쪽이동
        if ch == '<':
            if l_q:
                go_left(l_q, r_q)
        elif ch == '>':
            if r_q:
                go_right(l_q, r_q)
        elif ch == '-':
            if l_q:
                del_chr(l_q)
        else:
            l_q.append(ch)
    print("".join(l_q + r_q))