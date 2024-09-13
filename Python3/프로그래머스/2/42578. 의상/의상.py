def solution(clothes):
    clothes_count = {}
    for name, kind in clothes:
        if kind in clothes_count:
            clothes_count[kind] += 1
        else:
            clothes_count[kind] = 1
    answer = 1
    for count in clothes_count.values():
        answer *= (count + 1)
    return answer - 1