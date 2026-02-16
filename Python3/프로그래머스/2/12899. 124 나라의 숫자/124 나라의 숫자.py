def solution(n):
    reverse_list = []
    reverse_list.append(n)
    
    while reverse_list[-1] > 3:
        cur = reverse_list.pop()
        remain = cur % 3
        n_cur = cur // 3
        if remain == 0:
            remain = 4
            n_cur -= 1
        reverse_list.append(remain)
        reverse_list.append(n_cur)
    ans = list(map(str, reversed(reverse_list)))
    
    return ''.join(ans).replace('3', '4')