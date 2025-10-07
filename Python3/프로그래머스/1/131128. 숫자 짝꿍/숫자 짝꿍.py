from collections import Counter

def solution(X, Y):
    cnt_X = Counter(X)
    cnt_Y = Counter(Y)
    cnt_XY = cnt_X & cnt_Y
    result = "".join(sorted(list(cnt_XY.elements()), reverse = True))
    if result == "":
        return "-1"
    elif result.startswith("0"):
        return "0"
    else:
        return result
    
    