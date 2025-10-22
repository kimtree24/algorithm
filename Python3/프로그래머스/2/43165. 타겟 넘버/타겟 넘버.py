def solution(numbers, target):
    n = len(numbers)

    def dfs(i, total):
        # 종료 조건
        if i == n:
            return 1 if total == target else 0

        # 분기
        count = 0
        count += dfs(i + 1, total + numbers[i])
        count += dfs(i + 1, total - numbers[i])
        return count  # 현재 단계에서 가능한 모든 경우의 수 합

    return dfs(0, 0)