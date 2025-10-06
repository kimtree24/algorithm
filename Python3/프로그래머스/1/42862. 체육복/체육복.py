def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    overlap = lost & reserve
    lost -= overlap
    reserve -= overlap
    for r in sorted(reserve):
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)

    return n - len(lost)