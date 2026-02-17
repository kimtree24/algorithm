def solution(data, col, row_begin, row_end):
    # 정렬하기
    # S_i 구하기
    # 누적 합
    # bitwise XOR하기
    
    # 정렬하기
    sorted_data = sorted(data, key = lambda x : (x[col - 1], -x[0]))
    
    # S_i 구하기 + 누적 합
    XOR_S = 0
    for i in range(row_begin, row_end + 1): # row_begin이 1이면 index는 0임
        idx = i - 1 # index 보정
        target = sorted_data[idx]
        S_i = 0
        for col in target:
            S_i += col % i
        
        if i == row_begin:
            XOR_S = S_i
        else:
            XOR_S = XOR_S ^ S_i
    return  XOR_S
            
        
        