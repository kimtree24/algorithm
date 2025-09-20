def solution(s):
    index = {} # 각 글자별 가장 최근 인덱스 관리
    result = [] # return할 결과 저장
    
    # 각 char 별 판단
    for i in range(len(s)):
        # 해당 char이 한번도 판단 되지 않았다면
        if s[i] not in index:
            result.append(-1)
            index[s[i]] = i
            
        # 해당 char이 있다면
        elif s[i] in index:
            result.append(i - index.get(s[i]))
            index[s[i]] = i
    return result