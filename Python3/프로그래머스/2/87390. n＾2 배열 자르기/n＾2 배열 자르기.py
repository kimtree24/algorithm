def solution(n, left, right):
    result = []
    for each_idx in range(left, right + 1):
        y, x = divmod(each_idx, n)
        result.append(max(y, x) + 1)
    return result