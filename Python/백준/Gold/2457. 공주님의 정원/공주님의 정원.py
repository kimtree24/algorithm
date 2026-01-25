import sys
input = sys.stdin.readline

n = int(input().strip())
flowers = []

for _ in range(n):
    sm, sd, em, ed = map(int, input().strip().split())
    start = sm * 100 + sd
    end = em * 100 + ed
    flowers.append((start, end))
flowers.sort()

cur = 301
end = 1130
idx = 0
cnt = 0
max_end = 0

while cur <= end:
    flag = False
    
    while idx < n and flowers[idx][0] <= cur:
        if flowers[idx][1] > max_end:
            max_end = flowers[idx][1]
            flag = True
        idx += 1
    if not flag:
        cnt = 0
        break
    cnt += 1
    cur = max_end
print(cnt)