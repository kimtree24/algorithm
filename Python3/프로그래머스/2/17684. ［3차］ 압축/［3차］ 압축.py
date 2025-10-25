def solution(msg):
    dictionary = {chr(65 + i): i + 1 for i in range(26)}
    next_idx = 27
    result = []
    w = ""
    
    for c in msg:
        if w + c in dictionary:
            w = w + c
        else:
            result.append(dictionary[w])
            dictionary[w+c] = next_idx
            next_idx += 1
            w = c
    result.append(dictionary[w])
    return result
        