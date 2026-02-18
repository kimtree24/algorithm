def solution(diffs, times, limit):
    n = len(diffs)
    
    def cal(level):
        total = 0
        
        for i in range(n):
            if diffs[i] <= level:
                total += times[i]
            else:
                if i == 0:
                    time_prev = 0
                else:
                    time_prev = times[i - 1]
                total += (times[i] + time_prev) * (diffs[i] - level) + times[i]
            if total > limit:
                return False
        return True
    
    left, right = 1, max(diffs)
    ans = right
    
    while left <= right:
        mid = (left + right) // 2
        
        # 판단 로직
        if cal(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans
        