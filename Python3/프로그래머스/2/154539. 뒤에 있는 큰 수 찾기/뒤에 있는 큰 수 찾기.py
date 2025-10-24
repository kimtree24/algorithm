def solution(numbers):
    n = len(numbers)
    ans = [-1 for _ in range(n)]
    stack = []
    
    for idx, num in enumerate(numbers):
        while stack and num > numbers[stack[-1]]:
            j = stack.pop()
            ans[j] = num
        stack.append(idx)
    return ans