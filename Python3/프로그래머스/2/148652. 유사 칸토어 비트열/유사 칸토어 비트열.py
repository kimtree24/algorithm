def solution(n, l, r):
    def count(n, l, r):
        if n == 0:
            return 1
        
        length = 5 ** n
        unit = length // 5
        
        total = 0
        
        for i in range(5):
            start = i * unit + 1
            end = (i + 1) * unit
            
            if r < start or l > end:
                continue
            
            if i == 2:
                continue
                
            new_l = max(l, start) - start + 1
            new_r = min(r, end) - start + 1
            
            total += count(n - 1, new_l, new_r)
        return total
    
    return count(n, l, r)
            