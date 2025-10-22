def solution(dirs):
    # 방향 정의
    direction = {"U": (1, 0), "D": (-1, 0), "R": (0, 1), "L": (0, -1)}
    
    visit_way = set()
    
    row, col = 0, 0
    
    for i in dirs:
        nrow, ncol = direction[i][0] + row, direction[i][1] + col
        if -5 <= nrow <= 5 and -5 <= ncol <= 5:
            visit_way.add(((row, col), (nrow, ncol)))
            visit_way.add(((nrow, ncol), (row, col)))
            row, col = nrow, ncol
    return len(visit_way) // 2
        