def solution(sizes):
    init_row_max = 0
    init_col_max = 0
    max = 0
    row_col = -1 # 기준 잡을 것
    
    # 가로 세로 중 가장 큰 값 찾기
    for i in sizes:
        if init_row_max < i[0]:
            init_row_max = i[0]
        if init_col_max < i[1]:
            init_col_max = i[1]
        if init_row_max < init_col_max:
            max = init_col_max
            row_col = 1
        elif init_row_max >= init_col_max:
            max = init_row_max
            row_col = 0
        
    
    # 가로가 가장 큰 경우 가로 기준 뒤집고 세로에서 가장 큰 값 찾기
    if row_col == 0:
        col_max = 0
        
        for i in sizes:
            if i[0] < i[1]:
                # 뒤집기 로직
                temp = i[0]
                i[0] = i[1]
                i[1] = temp
            # col에서 가장 큰 값 찾기
            if i[1] > col_max:
                col_max = i[1]
        return max * col_max

                
    if row_col == 1:
        row_max = 0
        
        for i in sizes:
            if i[1] < i[0]:
                # 뒤집기 로직
                temp = i[0]
                i[0] = i[1]
                i[1] = temp
            # col에서 가장 큰 값 찾기
            if i[0] > row_max:
                row_max = i[0]
        print(row_col, max, row_max)
        return max * row_max
        
        
                
            
        