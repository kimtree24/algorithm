def solution(keyinput, board):
    x = 0 # 첫 시작 x 좌표
    y = 0 # 첫 시작 y 좌표
    
    max_x = (board[0]-1) / 2 # 게임판 최대 x 좌표
    min_x = 0-((board[0]-1)/2) # 게임판 최소 x 좌표
    max_y = (board[1]-1) / 2 # 게임판 최대 y 좌표
    min_y = 0-((board[1]-1)/2) # 게임판 최소 x 좌표
    
    for i in keyinput:
        if i == 'left' and x > min_x:
            x -= 1
        elif i == 'right' and x < max_x:
            x += 1
        elif i == 'up' and y < max_y:
            y += 1
        elif i == 'down' and y > min_y:
            y -= 1
        else:
            continue
    
    return [x,y]