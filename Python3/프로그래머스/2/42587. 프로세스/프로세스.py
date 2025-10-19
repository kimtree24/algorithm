from collections import deque

def solution(priorities, location):
    max_priority = max(priorities)
    
    priorities_q = deque(priorities)
    cnt = 0
    
    while priorities_q:
        process = priorities_q[0]
        # 실행
        if max_priority <= process:
            priorities_q.popleft()
            cnt += 1
            # 지금 찾고자 하는 값이라면
            if location == 0:
                return cnt
            # 실행시키면 location -1
            location -= 1
            # 최고 우선순위 갱신
            max_priority = max(priorities_q)
        # 후순위로
        else:
            priorities_q.popleft()
            priorities_q.append(process)
            # 지금 찾고자 하는 값이라면
            if location == 0:
                location += len(priorities_q) - 1
            # 후순위로 보내면 location -1
            else:
                location -= 1
    return 0
        