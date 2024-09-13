from collections import deque
def solution(elements) :
    a = []
    for i in range(1,len(elements)+1) :
        deq = deque(maxlen=i)
        for i in elements * 2 :
            deq.append(i)
            a.append(sum(deq))

    return(len(set(a)))