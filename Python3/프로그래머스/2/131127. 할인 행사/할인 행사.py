from collections import Counter

def solution(want, number, discount):
    need = {item: cnt for item, cnt in zip(want, number)}
    n = len(discount)
    W = 10
    result = 0
    
    # 판단할 리스트 초기화
    window = Counter(discount[:W])

    if all(window.get(k, 0) == need[k] for k in need):
        result += 1

    # 슬라이딩
    for i in range(W, n):
        out_item = discount[i - W]
        in_item  = discount[i]

        # 윈도우 갱신
        window[out_item] -= 1
        if window[out_item] == 0:
            del window[out_item]
        window[in_item] = window.get(in_item, 0) + 1

        # 필요 수량과 정확히 일치하는지 검사
        if all(window.get(k, 0) == need[k] for k in need):
            result += 1

    return result