def solution(order):
    stack = []
    cnt = 0
    max_order = len(order)
    idx = 0
    
    for box in range(1, max_order + 1):
        stack.append(box)
        while stack and stack[-1] == order[idx] and idx < max_order:
            stack.pop()
            cnt += 1
            idx += 1
    return cnt