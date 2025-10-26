def solution(n):
    MOD = 1000000007
    
    # DP 테이블 초기화
    dp = [0] * (n + 1)
    
    # 초기값
    dp[1] = 1
    if n >= 2:
        dp[2] = 2
    
    # 점화식
    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    
    return dp[n]