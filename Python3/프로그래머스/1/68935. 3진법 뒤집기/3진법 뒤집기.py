def solution(n):
    stack = []
    while (n != 0):
        stack.append(str(n % 3))
        n //= 3
    ans = ''.join(stack)
    return int(ans,3)
    