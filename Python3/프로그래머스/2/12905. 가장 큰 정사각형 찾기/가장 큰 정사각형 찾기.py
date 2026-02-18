def solution(board):
    r_len = len(board)
    c_len = len(board[0])
    
    size = 0
    
    for r in range(r_len):
        for c in range(c_len):
            if board[r][c] == 1:
                if r == 0 or c == 0:
                    size = max(size, 1)
                else:
                    board[r][c] = min(board[r-1][c-1], board[r][c-1], board[r-1][c]) + 1
                    size = max(size, board[r][c])
    return size * size