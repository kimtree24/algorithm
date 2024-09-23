def solution(board, h, w):
    count = 0
    color = board[h][w]
    if h > 0 and color == board[h-1][w]:
        count += 1
    if w > 0 and color == board[h][w-1]:
        count += 1
    if h < len(board)-1 and color == board[h+1][w]:
        count += 1
    if w < len(board)-1 and color == board[h][w+1]:
        count += 1
    return count