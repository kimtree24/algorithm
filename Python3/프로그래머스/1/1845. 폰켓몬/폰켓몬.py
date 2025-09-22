from itertools import combinations

def solution(nums):
    can_get = len(nums) // 2 # 가질 수 있는 포켓못 수
    
    nums_set = set(nums)
    print(nums, nums_set)
    
    if len(nums_set) > can_get:
        return can_get
    else:
        return len(nums_set)
        
    