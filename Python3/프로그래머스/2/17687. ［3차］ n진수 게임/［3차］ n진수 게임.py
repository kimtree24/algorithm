from collections import deque

def base(n, num):
    base_list = deque([])
    mock = num
    if mock == 0:
        base_list.appendleft(0)
    while mock > 0:
        remain = mock % n
        mock = mock // n
        base_list.appendleft(remain)
    return base_list

def solution(n, t, m, p):
    stream = []
    num = 0
    need = t * m
    while len(stream) < need:
        stream += base(n, num)
        num += 1

    idx = p - 1
    digits = "0123456789ABCDEF"
    ans = []
    for _ in range(t):
        ans.append(digits[stream[idx]])
        idx += m

    return "".join(ans)
        