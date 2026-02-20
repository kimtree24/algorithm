def combinations(n, r):
    target = [i for i in range(1, n + 1)]
    path = []
    ans = []
    
    def dfs(start):
        if len(path) == r:
            ans.append(path[:])
            return
        
        for i in range(start, n - (r - len(path)) + 1):
            path.append(target[i])
            dfs(i + 1)
            path.pop()
    dfs(0)
    return ans
            
def solution(n, q, ans):
    candinates = combinations(n, 5)
    m = len(ans)
    result = 0
    for candi in candinates:
        flag = True
        candi_set = set(candi)
        for i in range(m):
            if len(candi_set & set(q[i])) != ans[i]:
                flag = False
                break
        if flag:
            result += 1
    return result