def solution(storey: int) -> int:
    ans = 0
    while storey > 0:
        d = storey % 10
        next_d = (storey // 10) % 10

        if d < 5:
            ans += d
            storey //= 10
        elif d > 5:
            ans += (10 - d)
            storey = storey // 10 + 1
        else:
            if next_d >= 5:
                ans += 5
                storey = storey // 10 + 1
            else:
                ans += 5
                storey //= 10
    return ans