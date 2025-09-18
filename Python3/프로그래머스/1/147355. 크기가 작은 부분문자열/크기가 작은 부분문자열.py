def solution(t, p):
    result = 0
    
    p_len = len(p)
    
    p_int = int(p)
    
    for i in range(len(t)+1-p_len):
        cur_num = int(t[i:i+p_len])
        if p_int >= cur_num:
            result += 1
        else:
            continue
    return result