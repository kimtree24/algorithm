def solution(k, score):
    table = [] # 명예의 전당
    result = [] # 일일 최저점
    
    for i in score:
        # 명예의 전당 비어있다면 일단 다 넣음
        if len(table) < k:
            table.append(i)
            table.sort()
        # 명예의 전당 다 찼다면 가장 낮은 점수와 교체후 sort
        else:
            if table[0] < i:
                table[0] = i
                table.sort()
        # 최저점 기록
        result.append(table[0])
    return result
        