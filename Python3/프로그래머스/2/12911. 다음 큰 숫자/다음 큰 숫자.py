def solution(n):
    num_list = list(bin(n))[2:]
    count = num_list.count('1')
    ans = 0
    while n <= 1000000:
        n += 1
        new_num_list = list(bin(n))[2:]
        new_count = new_num_list.count('1')
        if new_count == count:
            ans = n
            break
    return ans