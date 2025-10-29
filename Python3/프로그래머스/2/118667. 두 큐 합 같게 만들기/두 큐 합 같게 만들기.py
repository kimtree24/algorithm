from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)
    
    total = s1 + s2
    
    if total % 2 == 1:
        return -1
    
    aim = total // 2
    
    ans = 0
    
    while ans <= (len(q1) + len(q2)) * 3:
        if s1 == aim:
            return ans
        if s1 > aim:
            x = q1.popleft()
            q2.append(x)
            s1 -= x
            s2 += x
        else:
            x = q2.popleft()
            q1.append(x)
            s1 += x
            s2 -= x
        ans += 1

    return -1