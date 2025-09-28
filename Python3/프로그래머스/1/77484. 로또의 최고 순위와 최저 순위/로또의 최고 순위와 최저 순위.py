def solution(lottos, win_nums):
    zero_cnt = lottos.count(0)
    min_cnt = len(set(lottos) & set(win_nums))
    max_cnt = min_cnt + zero_cnt
    
    def rank(n):
        return min(7 - n, 6)
    
    return [rank(max_cnt), rank(min_cnt)]