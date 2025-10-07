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
                
        if cur_doll == 0:
            continue

        if temp_saved and temp_saved[-1] == cur_doll:
            temp_saved.pop()
            crashed += 2
        else:
            temp_saved.append(cur_doll)

    return crashed