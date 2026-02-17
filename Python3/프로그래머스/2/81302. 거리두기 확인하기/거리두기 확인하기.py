def solution(places):
    ans = []
    
    for place in places:
        flag = 1
        
        for r in range(5):
            for c in range(5):
                if place[r][c] != 'P':
                    continue
                
                for dr in range(-2, 3):
                    for dc in range(-2, 3):
                        nr, nc = r + dr, c + dc
                        
                        if 0 <= nr < 5 and 0 <= nc < 5:
                            dist = abs(dr) + abs(dc)
                            
                            if dist == 0 or dist > 2:
                                continue
                            
                            if place[nr][nc] == 'P':
                                if dist == 1:
                                    flag = 0
                                
                                # 거리 2인 경우
                                elif dist == 2:
                                    # 같은 행
                                    if r == nr:
                                        if place[r][(c + nc)//2] != 'X':
                                            flag = 0
                                    
                                    # 같은 열
                                    elif c == nc:
                                        if place[(r + nr)//2][c] != 'X':
                                            flag = 0
                                    
                                    # 대각선
                                    else:
                                        if place[r][nc] != 'X' or place[nr][c] != 'X':
                                            flag = 0
                                
                        if flag == 0:
                            break
                    if flag == 0:
                        break
                if flag == 0:
                    break
        
        ans.append(flag)
    
    return ans