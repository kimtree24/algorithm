def solution(m, n, board):
    # 배열로 옮기기
    board_ = [['' for _ in range(n)] for _ in range(m)]
    for r in range(m):
        for c in range(n):
            board_[r][c] = board[r][c]
    total = 0
    
    while True:
        bomb = set()
    
        for r in range(m - 1):
            for c in range(n - 1):
                ch = board_[r][c]
                if ch == '0':
                    continue
                if board_[r+1][c] == ch and board_[r][c+1] == ch and board_[r+1][c+1] == ch:
                    bomb.update([(r, c), (r+1, c), (r, c+1), (r+1, c+1)])
                    
        if not bomb:
            break
            
        total += len(bomb)
        
        for r, c in bomb:
            board_[r][c] = '0'
        for c in range(n):
            empty = m - 1
            for r in range(m - 1, -1, -1):
                if board_[r][c] != '0':
                    board_[empty][c] = board_[r][c]
                    if empty != r:
                        board_[r][c] = '0'
                    empty -= 1
    return total
        
            