def solution(s):
    result = []
    words = s.split(' ')
    for word in words:
        if len(word) > 0:
            result.append(word[0].upper() + word[1:].lower())
        else:
            result.append('')
    return ' '.join(result)