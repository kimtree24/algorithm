from itertools import combinations

def solution(numbers):
    combi_set = set(combinations(numbers, 2))
    
    result = set()
    for each_combi in combi_set:
        result.add(sum(each_combi))
    
    return sorted(list(result))
        
    