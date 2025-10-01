def solution(keymap, targets):
    key_map = {'A':-1, 'B': -1,'C':-1, 'D': -1,'E':-1, 'F': -1,'G':-1, 'H': -1,'I':-1, 'J': -1,'K':-1, 'L': -1,'M':-1, 'N': -1,'O':-1, 'P': -1,'Q':-1, 'R': -1,'S':-1, 'T': -1,'U':-1, 'V': -1,'W':-1, 'X': -1,'Y':-1, 'Z': -1}
    for each_key in keymap:
        for i, each_char in enumerate(each_key):
            if key_map[each_char] != -1 and i+1 < key_map[each_char]:
                key_map[each_char] = i+1
            elif key_map[each_char] == -1:
                key_map[each_char] = i+1
    result = []
    for each_target in targets:
        each_sum = 0
        for each_char in each_target:
            if key_map[each_char] == -1:
                each_sum = -1
                break
            else:
                each_sum += key_map[each_char]
        result.append(each_sum)
    return result
        
        
    