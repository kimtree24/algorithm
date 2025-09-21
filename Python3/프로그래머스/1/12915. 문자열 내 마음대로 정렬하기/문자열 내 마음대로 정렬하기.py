def solution(strings, n):
    new_strings = [] # n번째 char 붙여서 새로 만든 문자열
    result = [] # 문자열 원복 저장용
    
    for each_str in strings:
        new_strings.append(each_str[n] + each_str) # 판단 문자열 생성
    
    new_strings.sort()
    
    # 원복
    for i in new_strings:
        result.append(i[1:])
    return result
    
        
        
        