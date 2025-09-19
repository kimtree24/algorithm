def solution(s):
    result = ''
    count = 0
    
    for ch in s:
        if ch == " ":
            result += " "
            count = 0
            continue

        if count % 2 == 0:
            result += ch.upper()
        else:
            result += ch.lower()
        count += 1

    return result