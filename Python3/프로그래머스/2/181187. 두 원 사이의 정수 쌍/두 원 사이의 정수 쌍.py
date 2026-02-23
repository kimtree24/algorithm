import math

def solution(r1, r2):
    answer = 0
    
    for x in range(0, r2 + 1):
        # 큰 원에서 가능한 y 최대값
        max_y = int(math.sqrt(r2*r2 - x*x))
        
        # 작은 원 내부는 제외
        if x < r1:
            min_y = math.ceil(math.sqrt(r1*r1 - x*x))
        else:
            min_y = 0
        
        if max_y >= min_y:
            answer += (max_y - min_y + 1)
    return answer * 4 - (r2 - r1 + 1) * 4