def solution(n,a,b):
    count = 0
    while abs(a-b) >= 1:
        if a % 2 !=0:
            a = a//2 + 1
        else:
            a = a//2
        if b % 2 !=0:
            b = b//2 + 1
        else:
            b = b//2
        count += 1
    return count