def solution(park, routes):
    
    len_row = len(park) # 컬럼 길이 (세로)
    len_col = len(park[0]) # 행 길이 (가로)
    
    start = None
    not_point = set() # 장애물 위치
    
    for idx_row, row in enumerate(park):
        for idx_col, each_point in enumerate(row):
            if each_point == "S":
                start = (idx_row, idx_col)
            elif each_point == "X":
                not_point.add((idx_row, idx_col))
                
    directions_set = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    
    row, col = start
    
    for move in routes:
        direction, num_str = move.split()
        num = int(num_str)
        d_row, d_col = directions_set[direction]
        
        now_row, now_col = row, col
        
        flag = True
        
        for i in range(num):
            now_row += d_row
            now_col += d_col
            if not (0 <= now_row < len_row and 0 <= now_col < len_col) or (now_row, now_col) in not_point:
                flag = False
                break
        if flag:
            row, col = now_row, now_col
            
    
    return [row, col]