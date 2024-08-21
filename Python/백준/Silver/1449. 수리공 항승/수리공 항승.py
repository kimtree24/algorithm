import sys
n, l = map(int, sys.stdin.readline().rstrip().split())

loca = list(map(int, sys.stdin.readline().rstrip().split()))
loca.sort()

start = 0
count = 0

while start < n:
    count += 1
    endPoint = loca[start] - 0.5 + l

    while start < n and loca[start] + 0.5 <= endPoint:
        start += 1
print(count)