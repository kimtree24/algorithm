def solution(picks, minerals):
    # 5개씩 묶기
    # 빡센 것 순으로 정렬
    # 좋은 것 부터 배정
    # 결과 계산
    
    # 5개씩 묶기
    groups = []
    max_groups = sum(picks)
    
    for i in range(0,len(minerals), 5):
        if len(groups) == max_groups:
            break
        groups.append(minerals[i : i + 5])
    
    # 빡센 것 계산
    score_list = []
    for group in groups:
        score = 0
        n_dia = 0
        n_iron = 0
        n_stone = 0
        for mineral in group:
            if mineral == 'diamond':
                score += 3
                n_dia += 1
            elif mineral == 'iron':
                score += 2
                n_iron += 1
            elif mineral == 'stone':
                score += 1
                n_stone += 1
        score_list.append([n_dia, n_iron, n_stone, score])
    # 정렬
    sorted_groups = sorted(score_list, key = lambda x: (x[0], x[1], x[2]), reverse = True)
    
    # 답
    ans = 0
    
    # 배정
    n_dia_pick, n_iron_pick, n_stone_pick = picks
    for dia, iron, stone, _ in sorted_groups:
        if n_dia_pick > 0:
            n_dia_pick -= 1
            ans += dia + iron + stone
        elif n_iron_pick > 0:
            n_iron_pick -= 1
            ans += dia * 5 + iron + stone
        elif n_stone_pick > 0:
            n_stone_pick -= 1
            ans += dia * 25 + iron * 5 + stone
        else:
            break
    return ans