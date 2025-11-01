from collections import Counter

def solution(weights):
    cnt = Counter(weights)
    ans = 0
    for c in cnt.values():
        ans += c * (c - 1) // 2
    ratios = [(2, 3), (1, 2), (3, 4)]
    for w, c in cnt.items():
        for a, b in ratios:
            num = w * a
            if num % b == 0:
                t = num // b
                if t in cnt and t < w:
                    ans += c * cnt[t]

    return ans