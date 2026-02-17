import math

def solution(n, k):
    nums = list(range(1, n + 1))
    ans = []
    
    k -= 1
    
    for i in range(n, 0, -1):
        fact = math.factorial(i - 1)
        idx = k // fact
        ans.append(nums.pop(idx))
        k %= fact
    return ans