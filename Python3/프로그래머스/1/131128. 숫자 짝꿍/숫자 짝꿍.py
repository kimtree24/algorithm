from collections import Counter

def solution(X, Y):
    cntX = Counter(X)
    cntY = Counter(Y)

    parts = []
    for d in '9876543210':
        k = min(cntX[d], cntY[d])
        if k:
            parts.append(d * k)

    if not parts:
        return "-1"

    ans = "".join(parts)
    return "0" if ans[0] == "0" else ans