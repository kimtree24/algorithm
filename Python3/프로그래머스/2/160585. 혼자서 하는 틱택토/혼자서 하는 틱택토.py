def solution(board):
    cnt_O = 0
    cnt_X = 0
    
    for r in range(3):
        for c in range(3):
            if board[r][c] == 'O':
                cnt_O += 1
            elif board[r][c] == 'X':
                cnt_X += 1
    
    # 개수 조건
    if not (cnt_O == cnt_X or cnt_O == cnt_X + 1):
        return 0
    
    def win(ch):
        for r in range(3):
            if all(board[r][c] == ch for c in range(3)):
                return True
        for c in range(3):
            if all(board[r][c] == ch for r in range(3)):
                return True
        
        if all(board[i][i] == ch for i in range(3)):
            return True
        if board[0][2] == ch and board[1][1] == ch and board[2][0] == ch:
            return True
        return False
    
    winO = win('O')
    winX = win('X')
    
    # 둘 다 승리 불가
    if winO and winX:
        return 0
    # O 승리시 cnt는 O가 무조건 + 1
    if winO and cnt_O - 1 != cnt_X:
        return 0
    # X 승리시 cnt는 O와 X가 동일
    if winX and cnt_O != cnt_X:
        return 0
    return 1
    
    