def solution(n):
    num_list = []
    for i in range(1, n + 1):
        num_list.append(i)
    pointer1 = 0
    pointer2 = 1
    count = 0
    while pointer1 < n:
        if sum(num_list[pointer1:pointer2]) < n:
            pointer2 += 1
        elif sum(num_list[pointer1:pointer2]) == n:
            count += 1
            pointer1 += 1
            pointer2 = pointer1
        else:
            pointer1 += 1
            pointer2 = pointer2
    return count