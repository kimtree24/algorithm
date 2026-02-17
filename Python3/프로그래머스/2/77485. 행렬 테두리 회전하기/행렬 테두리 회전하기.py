def solution(rows, columns, queries):
    # 좌표계 만들기
    # queries for문으로 돌면서 시뮬레이션
    # 시뮬레이션 돌리기 전 시뮬레이션 돌 숫자들 기억하기 -> 여기서 가장 작은 것 ans에 담기
    
    # 좌표계 만들기
    board = [[i + (j * columns) for i in range(1, columns + 1)] for j in range(rows)]
    
    ans = []
    
    # 시뮬레이션
    for query in queries:
        x1, y1, x2, y2 = query
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        
        prev = board[x1][y1]
        min_value = prev
        
        for c in range(y1 + 1, y2 + 1):
            board[x1][c], prev = prev, board[x1][c]
            min_value = min(min_value, prev)
        for r in range(x1 + 1, x2 + 1):
            board[r][y2], prev = prev, board[r][y2]
            min_value = min(min_value, prev)
        for c in range(y2 - 1, y1 - 1, -1):
            board[x2][c], prev = prev, board[x2][c]
            min_value = min(min_value, prev)
        for r in range(x2 - 1, x1 - 1, -1):
            board[r][y1], prev = prev, board[r][y1]
            min_value = min(min_value, prev)
        
        ans.append(min_value)
    return ans