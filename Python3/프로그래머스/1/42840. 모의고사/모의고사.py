def solution(answers):
    _1 = [1,2,3,4,5]
    _2 = [2,1,2,3,2,4,2,5]
    _3 = [3,3,1,1,2,2,4,4,5,5]
    
    idx_1, idx_2, idx_3 = 0,0,0
    ans_num = {1:0, 2:0, 3:0}
    
    for i in range(len(answers)):
        if answers[i] == _1[idx_1]:
            ans_num[1] += 1
        if idx_1 < 4:
            idx_1 += 1
        else:
            idx_1 = 0
                
        if answers[i] == _2[idx_2]:
            ans_num[2] += 1
        if idx_2 < 7:
            idx_2 += 1
        else:
            idx_2 = 0
            
        if answers[i] == _3[idx_3]:
            ans_num[3] += 1
        if idx_3 < 9:
            idx_3 += 1
        else:
            idx_3 = 0
    
    max_key = max(ans_num, key = ans_num.get)
    result = []
    if ans_num[max_key] == ans_num[1]:
        result.append(1)
    if ans_num[max_key] == ans_num[2]:
        result.append(2)
    if ans_num[max_key] == ans_num[3]:
        result.append(3)
    return result
    
        