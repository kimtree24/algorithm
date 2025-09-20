def solution(s, n):
    answer = ''
    
    for i in s:
        cur_char = ord(i)
        next_char = cur_char + n
        
        # 공백 처리
        if i == " ":
            answer += " "
            
        # 대문자
        elif cur_char <= 90 and cur_char >=65:
            if next_char <= 90:
                answer += chr(next_char)
            else:
                answer += chr(next_char - 90 + 64)
        # 소문자
        elif cur_char <= 122 and cur_char >= 97 :
            if next_char <= 122:
                answer += chr(next_char)
            else:
                answer += chr(next_char - 122 + 96)
        
    return answer