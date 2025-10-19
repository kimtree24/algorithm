from collections import deque

def solution(priorities, location):
    q = deque([(p, i) for i, p in enumerate(priorities)])
    sorted_priorities = sorted(priorities, reverse=True)
    order = 0

    while q:
        cur = q.popleft()
        if cur[0] == sorted_priorities[order]:
            order += 1
            if cur[1] == location:
                return order
        else:
            q.append(cur)