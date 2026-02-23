def solution(n, info):
    best_diff = [0]
    ans = [-1]
    
    def dfs(idx, arrows_left, ryan):
        nonlocal ans
        # 끝내는 조건
        if idx == 11:
            # 남은 화살은 맨 마지막에 몰빵
            ryan[10] += arrows_left
            
            # 점수 계산
            a_score = 0
            r_score = 0
            
            for i in range(11):
                if ryan[i] == 0 and info[i] == 0:
                    continue
                if ryan[i] > info[i]:
                    r_score += 10 - i
                else:
                    a_score += 10 - i
                    
            diff = r_score - a_score
            
            if diff > 0:
                if diff > best_diff[0]:
                    best_diff[0] = diff
                    ans = ryan[:]
                elif diff == best_diff[0]:
                    for i in range(10, -1, -1):
                        if ryan[i] > ans[i]:
                            ans = ryan[:]
                        elif ryan[i] < ans[i]:
                            break
            
            ryan[10] -= arrows_left
            return
        
        # 다음 분기
        # 이번 것 이기는 경우
        need = info[idx] + 1
        if arrows_left >= need:
            arrows_left -= need
            ryan[idx] = need
            dfs(idx + 1, arrows_left, ryan)
            ryan[idx] = 0
            arrows_left += need

        # 이번 것 지는 경우
        dfs(idx + 1, arrows_left, ryan)
    
    dfs(0, n, [0 for _ in range(11)] )
    
    return ans