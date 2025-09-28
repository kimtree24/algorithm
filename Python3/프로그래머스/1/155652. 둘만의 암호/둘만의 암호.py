def solution(s, skip, index):
    char_list = [chr(i) for i in range(97,123,1)]
    for char in skip:
        char_list.remove(char)
    result = []
    for i in s:
        char_idx = char_list.index(i)
        exchanged_idx = (char_idx + index) % len(char_list)
        result.append(char_list[exchanged_idx])
    return ''.join(result)
        