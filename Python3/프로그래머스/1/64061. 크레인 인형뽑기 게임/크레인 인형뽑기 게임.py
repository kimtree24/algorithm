def solution(board, moves):
    temp_saved = []
    crashed = 0
    board_len = len(board)
    
    # 각 회차 판단
    for i in moves:
        # 각 회차별 컬럼 깊이 판단
        cur_doll = 0
        for row in range(board_len):
            if board[row][i-1] != 0:
                cur_doll = board[row][i-1]
                board[row][i-1] = 0
                break
        if cur_doll != 0:  
            temp_saved.append(cur_doll)
            
        if len(temp_saved) > 1:
            before_doll = temp_saved[-2]
            if cur_doll == before_doll:
                crashed += 2
                temp_saved.pop()
                temp_saved.pop()
    return crashed