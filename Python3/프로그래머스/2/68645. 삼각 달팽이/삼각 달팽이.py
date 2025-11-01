def solution(n):
    space = [[0] * (i + 1) for i in range(n)]
    dire = [(1,0), (0,1), (-1,-1)]
    
    total = 0
    for i in range(1, n+1):
        total += i
    
    cur_num = 1
    cur_dire = 0
    crow, ccol = 0,0
    
    while cur_num <= total:
        space[crow][ccol] = cur_num
        cur_num += 1
        nrow, ncol = crow + dire[cur_dire][0], ccol + dire[cur_dire][1]
        
        if not (0 <= nrow < n and 0 <= ncol < len(space[nrow])) or space[nrow][ncol] != 0:
            cur_dire = (cur_dire + 1) % 3
            nrow, ncol = crow + dire[cur_dire][0], ccol + dire[cur_dire][1]
        crow, ccol = nrow, ncol
    
    ans = []
    for row in space:
        for col in row:
            ans.append(col)
    return ans