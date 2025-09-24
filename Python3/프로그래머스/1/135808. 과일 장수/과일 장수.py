def solution(k, m, score):
    score_sorted = sorted(score, reverse=True)
    result_sum = 0

    for i in range(m-1, len(score), m):
        result_sum += score_sorted[i]

    return result_sum * m