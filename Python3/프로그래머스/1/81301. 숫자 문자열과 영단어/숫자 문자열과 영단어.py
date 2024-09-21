def solution(s):
    num_list = ['zero','one','two','three','four','five','six','seven', 'eight', 'nine']
    
    temp = []
    ans = []
    
    for i in range(len(s)):
        if 48<=ord(s[i])<=57:
            ans.append(s[i])
        else:
            temp.append(s[i])
            
        temp_str = ''.join(temp)
        if temp_str in num_list:
            ans.append(str(num_list.index(temp_str)))
            temp = []
    return int(''.join(ans))
            
        
        