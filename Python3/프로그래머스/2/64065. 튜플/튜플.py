def solution(s):
    s = s[1:len(s)-1]
    s_list = []
    temp_word = []
    for ch in s:
        if ch == '}':
            temp_word.append(ch)
            each_set = ''.join(temp_word)
            s_list.append(each_set)
        elif ch == "{":
            temp_word = ["{"]
        else:
            temp_word.append(ch)
    sorted_s = sorted(s_list, key = len)
    
    result = []
    
    for each_set in sorted_s:
        each_set = each_set[1: len(each_set) - 1]
        each_num_list = each_set.split(',')
        
        for each_num in each_num_list:
            int_each_num = int(each_num)
            if int(each_num) not in result:
                result.append(int_each_num)
    return result
        
    