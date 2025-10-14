from itertools import permutations

def solution(k, dungeons):
    
    permutation_list = list(permutations(dungeons))
    
    result = 0
    
    for case in permutation_list:
        case_k = k
        case_result = 0
        for dungeon in case:
            limit_p, use_p = dungeon
            
            if case_k >= limit_p:
                case_k -= use_p
                case_result += 1
            else:
                break
        
        if result < case_result:
            result = case_result
    return result
            
        