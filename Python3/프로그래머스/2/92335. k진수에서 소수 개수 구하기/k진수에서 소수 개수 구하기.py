from collections import deque
import math

def transfer(n, k):
    # 진법 변환
    mock = n
    string = deque([])
    while mock > 0:
        remain = mock % k
        mock = mock // k
        string.appendleft(str(remain))
    return ''.join(string)

def is_prime(num):
    if num <= 1:
        return False
    sqrt_num = math.sqrt(num)
    for i in range(2, int(sqrt_num) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    trans = transfer(n, k)
    parts = trans.split('0')
    ans = 0
    for p in parts:
        if not p:
            continue
        num = int(p)
        if is_prime(num):
            ans += 1
    return ans