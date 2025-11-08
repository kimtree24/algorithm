import sys
input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    arr = []
    def dfs(start):
        if len(arr) == 6:
            print(*arr)
            return
        for i in range(start, nums[0]+1):
            arr.append(nums[i])
            dfs(i+1)
            arr.pop()
    dfs(1)
    print()