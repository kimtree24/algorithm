def solution(sequence, k):
    best_len = len(sequence)
    best = [0,best_len-1]
    start = 0
    
    cur_sum = 0
    
    for end in range(len(sequence)):
        cur_sum += sequence[end]
        
        while cur_sum >= k and start <= end:
            if cur_sum == k:
                cur_len = end-start+1
                if (cur_len < best_len) or (cur_len == best_len and start < best[0]):
                    best_len = cur_len
                    best = [start, end]
            cur_sum -= sequence[start]
            start += 1
    return best