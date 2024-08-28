import sys
n, m, b = map(int, sys.stdin.readline().rstrip().split())
matrix = []
minHigh = 256
maxHigh = 0
for _ in range(n):
    line = list(map(int,sys.stdin.readline().rstrip().split()))
    matrix.append(line)
    minHigh = min(minHigh, min(line))
    maxHigh = max(maxHigh, max(line))

ansTime = 1e9
bestHigh = 0

for refHigh in range(minHigh, maxHigh+1):
    nowTime = 0
    blockAdd = 0
    blockDel = 0
    
    for i in range(n):
        for j in range(m):
            diff = matrix[i][j] - refHigh
            if diff > 0:
                nowTime += diff*2
                blockDel += diff
            elif diff < 0:
                nowTime += abs(diff)
                blockAdd += abs(diff)
                
    if b+blockDel-blockAdd >= 0 :
        if nowTime < ansTime:
            ansTime = nowTime
            bestHigh = refHigh
        elif nowTime == ansTime:
            bestHigh = max(bestHigh, refHigh)
print(ansTime, bestHigh)