def solution(n):
    list_sosu = [0] * (n + 1)
    
    for i in range(1,n+1):
        for j in range(i, n+1, i):
            list_sosu[j] += 1
    return list_sosu.count(2)
    