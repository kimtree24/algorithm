def solution(d, budget):
    d.sort()
    count = 0
    for i in d:
        budget -=i
        if budget < 0:
            break
        else:
            count+=1
    return count