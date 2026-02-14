def solution(orders, course):
    
    ans = []
    
    for i in range(len(orders)):
        orders[i] = ''.join(sorted(orders[i]))
    
    def make_combi(order, start, path, length, counter):
        if len(path) == length:
            key = ''.join(path)
            if key in counter:
                counter[key] += 1
            else:
                counter[key] = 1
            return
        for i in range(start, len(order)):
            path.append(order[i])
            make_combi(order, i + 1, path, length, counter)
            path.pop()
    
    for length in course:
        counter = {}
        
        for order in orders:
            if len(order) < length:
                continue
            make_combi(order, 0, [], length, counter)
        
        max_cnt = 0
        
        if counter:
            max_cnt = max(counter.values())
        
        if max_cnt < 2:
            continue
        
        for key in counter:
            if counter[key] == max_cnt:
                ans.append(key)
    ans.sort()
    return ans