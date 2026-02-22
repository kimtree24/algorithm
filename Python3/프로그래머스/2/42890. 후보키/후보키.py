def is_subset(small, big):
    for x in small:
        if x not in big:
            return False
    return True

def combinations(target, r):
    n = len(target)
    path = []
    ans = []
    
    def dfs(start):
        if len(path) == r:
            ans.append(path[:])
            return
        
        for i in range(start, n - (r - len(path)) + 1):
            path.append(target[i])
            dfs(i + 1)
            path.pop()
    dfs(0)
    return ans
    

def solution(relation):
    r_len = len(relation)
    c_len = len(relation[0])
    
    # 컬럼 키 조합 찾기
    target = [i for i in range(c_len)]
    col_keys = []
    for i in range(1, c_len + 1):
        keys = combinations(target, i)
        for key in keys:
            col_keys.append(key)
    result_list = []
    for col_key in col_keys: # 컬럼 셋
        # 키 별로 카운트 세기
        counter = {}
        for r in range(r_len):
            value = [] # 이게 하나의 판단할 값
            for col in col_key: # 각 컬럼 순회
                value.append(relation[r][col])
            key = ','.join(value)
            if not counter.get(key):
                counter[key] = 0
            counter[key] += 1
        can_key = True
        values = counter.values()
        for value in values:
            if value != 1:
                can_key = False
                break
        if can_key:
            result_list.append(col_key)
    
    # 최소성 판별
    final_keys = []
    
    for key in result_list:
        is_sub = True
        for fk in final_keys:
            # 서브셋이면 추가 안함
            if is_subset(fk, key):
                is_sub = False
                break
        if is_sub:
            final_keys.append(key)
        
    return len(final_keys)