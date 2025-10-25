def solution(land):
    for r in range(1, len(land)):
        for c in range(4):
            land[r][c] += max(land[r-1][k] for k in range(4) if k != c)
    return max(land[-1])