t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())

    lis_floor = []
    for i in range(1, n + 1):
        lis_floor.append(i)

    for _ in range(k):
        next_floor = [0]*n
        for i in range(n):
            next_floor[i] = sum(lis_floor[:i])+lis_floor[i]
        lis_floor = next_floor
    print(lis_floor[n - 1])