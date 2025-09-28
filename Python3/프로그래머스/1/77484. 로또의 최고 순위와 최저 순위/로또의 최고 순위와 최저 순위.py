def solution(lottos, win_nums):
    min_cnt = 0
    zero_cnt = 0
    max_cnt = 0
    for i in lottos:
        if i == 0:
            zero_cnt += 1
        else:
            if i in win_nums:
                min_cnt += 1
            else:
                continue
    max_cnt = min_cnt + zero_cnt
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    result = [rank.get(max_cnt), rank.get(min_cnt)]
    
    return result
    
        