def solution(X, Y):
    cnt_X = [0] * 10
    cnt_Y = [0] * 10
    
    for ch in X:
        cnt_X[ord(ch) - 48] += 1
    for ch in Y:
        cnt_Y[ord(ch) - 48] += 1
    
    result = []
    for i in range(9, -1, -1):
        k = min(cnt_X[i], cnt_Y[i])
        if k > 0:
            result.append(str(i) * k)
    result_str = "".join(result)
    
    if not result:
        return "-1"
    elif result_str[0] == "0":
        return "0"
    else:
        return result_str
            