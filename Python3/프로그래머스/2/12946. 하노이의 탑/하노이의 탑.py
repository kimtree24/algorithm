def solution(n):
    ans = []
    
    def move(n, start, mid, end):
        if n == 1:
            ans.append([start, end])
            return
        
        move(n - 1, start, end, mid)
        
        ans.append([start, end])
        
        move(n - 1, mid, start, end)
    move(n, 1, 2, 3)
    return ans
    