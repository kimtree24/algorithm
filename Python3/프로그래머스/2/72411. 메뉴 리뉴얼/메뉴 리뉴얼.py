from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    
    ans = []
    
    for n_course in course:
        # 각 조합 key
        each_course = defaultdict(int)
        
        for order in orders:
            order = sorted(order)
            combi = combinations(order, n_course)
            for e_combi in combi:
                combi_key = ''.join(e_combi)
                each_course[combi_key] += 1
        
        if not each_course:
            continue
        
        max_cnt = max(each_course.values())
        
        if max_cnt < 2:
            continue
        
        for menu, cnt in each_course.items():
            if cnt == max_cnt:
                ans.append(menu)
    ans.sort()
    return ans