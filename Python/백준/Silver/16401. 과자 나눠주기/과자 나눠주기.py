import sys
input = sys.stdin.readline

m, n = map(int, input().strip().split())
snacks = list(map(int, input().strip().split()))

left, right = 1, max(snacks)
answer = 0

while left <= right:
    mid = (left + right) // 2
    
    cnt = 0
    for each_snack in snacks:
        cnt += each_snack // mid
        
    if cnt >= m:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)