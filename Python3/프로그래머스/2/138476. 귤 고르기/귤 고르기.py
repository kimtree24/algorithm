from collections import Counter

def solution(k, tangerine):
    sizeList = Counter(tangerine)
    countList = sorted(sizeList.values(), reverse = True)
    
    total = 0
    count = 0
    
    for i in countList:
        total += i
        count += 1
        if total >= k:
            break
    return count
    
    return count