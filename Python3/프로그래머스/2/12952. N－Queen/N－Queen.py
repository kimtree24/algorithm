def solution(n):
    ans = 0

    # 열, 대각선1(/), 대각선2(\) 공격 여부
    col = [False] * n
    diag1 = [False] * (2 * n)      # r + c
    diag2 = [False] * (2 * n)      # r - c + n

    def dfs(r):
        nonlocal ans

        # 모든 행에 퀸을 놓았으면 성공
        if r == n:
            ans += 1
            return

        for c in range(n):
            if not col[c] and not diag1[r + c] and not diag2[r - c + n]:
                col[c] = True
                diag1[r + c] = True
                diag2[r - c + n] = True

                dfs(r + 1)

                col[c] = False
                diag1[r + c] = False
                diag2[r - c + n] = False

    dfs(0)
    return ans