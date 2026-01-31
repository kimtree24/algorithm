import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
trees = list(map(int, input().strip().split()))

left, right = 1, max(trees)
ans = 0
while left <= right:
    mid = (left + right) // 2
    cuted = 0
    for tree in trees:
        this_cut = tree - mid
        if this_cut > 0:
            cuted += this_cut
    if cuted >= m:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)