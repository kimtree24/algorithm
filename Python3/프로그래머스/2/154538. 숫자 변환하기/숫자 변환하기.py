from collections import deque

def solution(x, y, n):
    q = deque([(x,0)])
    visit = {x}
    
    while q:
        cur_x, cur_cnt = q.popleft()
        if cur_x == y:
            return cur_cnt
        for next_x in (cur_x + n, cur_x * 2, cur_x * 3):
            if next_x == y:
                return cur_cnt + 1
            if next_x < y and next_x not in visit:
                q.append([next_x, cur_cnt + 1])
                visit.add(next_x)
    return -1
    