import math
def solution(number, limit, power):
    
    result = 0
    
    for num_knight in range(1,number+1):
        # 지금 해당 기사의 약수 개수(가질 수 있는 공격력)
        sqrt_num = int(math.sqrt(num_knight))
        att_num = 0
        for j in range(1,sqrt_num+1):
            if num_knight % j == 0:
                att_num += 1
        att_num *= 2
        if math.sqrt(num_knight) == sqrt_num:
            att_num -= 1
        
        # 구매하는 무기 제한
        if att_num > limit:
            att_num = power
        
        result += att_num
    return result
        