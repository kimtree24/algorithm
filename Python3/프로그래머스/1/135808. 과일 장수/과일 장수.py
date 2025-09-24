def solution(k, m, score):
    num_box = len(score) // m
    
    score_sorted = sorted(score, reverse = True)
    
    idx = 0
    
    result_sum = 0
    
    for i in range(num_box):
        this_box = score_sorted[idx:idx+m]
        result_sum += this_box[-1]
        idx += m
    return result_sum * m