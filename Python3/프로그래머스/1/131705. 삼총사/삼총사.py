from itertools import combinations

def solution(number):
    
    result = 0
    
    # 삼총사 조합
    combi_list = list(combinations(number,3))
    
    for i in combi_list:
        sum_result = sum(i) # 각 조합에 대한 합계
        
        if (sum_result == 0):
            result += 1
        else:
            continue
    
    return result