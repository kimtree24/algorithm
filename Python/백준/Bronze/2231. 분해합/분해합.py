n = int(input())

for i in range(1, n+1):
    sum_num = sum(map(int, str(i)))
    all_sum = i + sum_num
    
    if all_sum == n:
        print(i)
        break
    if n == i:
        print(0)

