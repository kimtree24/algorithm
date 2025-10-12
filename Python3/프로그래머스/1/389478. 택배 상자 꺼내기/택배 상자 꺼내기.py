def solution(n, w, num):
    r = (num - 1) // w
    p = (num - 1) % w
    if r % 2 == 0:
        c = p
    else:
        c = w - 1 - p

    r_max = (n - 1) // w
    m = n % w  # 마지막 행 칸수(0이면 가득 참)

    if m == 0:
        last_has_c = True
    else:
        if r_max % 2 == 0:
            last_has_c = (c < m)
        else:
            last_has_c = (c >= w - m)

    ans = (r_max - r + 1) - (0 if last_has_c else 1)
    return ans