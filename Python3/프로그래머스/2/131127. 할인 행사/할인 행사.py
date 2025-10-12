def solution(want, number, discount):
    result = 0
    last_idx = 9
    while last_idx < len(discount):
        # 필요 물품 수량 체크
        stuff_dict = {stuff: number[idx] for idx, stuff in enumerate(want)}
        
        flag = True
        
        # 매번 10개 판단하기 위함
        start_idx = last_idx - 9
        
        parsed_list = discount[start_idx: last_idx + 1]
        for each_discount in parsed_list:
            if each_discount in want and stuff_dict[each_discount] > 0:
                stuff_dict[each_discount] -= 1
            else:
                flag = False
                break
        
        if flag:
            result += 1
        
        last_idx += 1
    return result