from collections import Counter

def solution(topping):
    right = Counter(topping)
    left = set()
    ans = 0
    for i in range(len(topping) - 1):
        x = topping[i]
        left.add(x)
        right[x] -= 1
        if right[x] == 0:
            del right[x]
        if len(left) == len(right):
            ans += 1
    return ans