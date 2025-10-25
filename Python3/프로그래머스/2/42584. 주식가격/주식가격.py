def solution(prices):
    ans = [0 for _ in range(len(prices))]
    
    stack = []
    
    for idx, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            ans[j] = idx - j
        stack.append(idx)
    while stack:
        j = stack.pop()
        ans[j] = len(prices) - j - 1
    return ans
        