import sys
k, n = map(int, sys.stdin.readline().rstrip().split())
len_k = []
for i in range(k):
    len_k.append(int(input()))
start = 1
end = max(len_k)
while  start <=end :
    mid = (start + end) // 2
    all_n = 0
    for i in len_k:
        all_n += i//mid
    if all_n < n:
        end = mid-1
    else:
        start = mid+1

print(end)