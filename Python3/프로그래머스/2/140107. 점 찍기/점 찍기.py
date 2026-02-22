import math
def cal_dist(x, d):
    y = math.floor(math.sqrt(d**2 - x**2))
    return y

def solution(k, d):
    # x축 fix하면 y축 max 값이 나옴 -> 그 안에 점 count
    cnt = 0
    for x in range(0, d+1, k):
        max_y = cal_dist(x, d)
        cnt += (max_y // k) + 1
    return cnt
    