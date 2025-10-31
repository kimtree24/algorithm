def solution(arr):
    n = len(arr)
    ans = [0, 0]
    
    def dfs(r, c, size):

        first = arr[r][c]
        flag = True
        for i in range(r, r + size):
            for j in range(c, c + size):
                if arr[i][j] != first:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            ans[first] += 1
            return
        half = size // 2
        dfs(r, c, half)
        dfs(r, c + half, half)
        dfs(r + half, c, half)
        dfs(r + half, c + half, half)

    dfs(0, 0, n)
    return ans