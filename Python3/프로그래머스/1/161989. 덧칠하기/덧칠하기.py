def solution(n, m, section):
    cnt = 0
    i = 0
    while i < len(section):
        start = section[i]
        end = start + m - 1
        cnt += 1
        
        while i < len(section) and section[i] <= end:
            i += 1
    return cnt