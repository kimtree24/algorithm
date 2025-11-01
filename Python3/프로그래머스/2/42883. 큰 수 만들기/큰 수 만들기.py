def solution(number, k):
    stack = []
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            k -= 1
            stack.pop()
        stack.append(num)
    
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)