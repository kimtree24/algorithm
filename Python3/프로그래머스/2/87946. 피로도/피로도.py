def solution(k, dungeons):
    n = len(dungeons)
    used = [False] * n

    def dfs(energy, cnt):
        max_cnt = cnt
        for i in range(n):
            need, cost = dungeons[i]
            if not used[i] and energy >= need:
                used[i] = True
                max_cnt = max(max_cnt, dfs(energy - cost, cnt + 1))
                used[i] = False
        return max_cnt

    return dfs(k, 0)