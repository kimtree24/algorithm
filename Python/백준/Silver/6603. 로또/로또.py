import sys
input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    K = nums[0]
    S = nums[1:]
    arr = []
    def dfs(start):
        if len(arr) == 6:
            print(*arr)
            return
        for i in range(start, K):
            arr.append(S[i])
            dfs(i+1)
            arr.pop()
    dfs(0)
    print()