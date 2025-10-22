def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    
    cnt = [0]
    
    def dfs(cnt, s):
        for ch in alpha:
            new_s = s + ch
            cnt[0] += 1
            if new_s == word:
                return True
            if len(new_s) < 5:
                if dfs(cnt, new_s):
                    return True
        return False

    dfs(cnt, "")
    return cnt[0]