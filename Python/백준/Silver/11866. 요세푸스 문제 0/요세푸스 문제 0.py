import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
lis = [i for i in range(1, n + 1)]
ans = []
idx = 0
while len(lis) > 0:
    idx = (idx + k - 1) % len(lis)
    ans.append(lis.pop(idx))

print('<' + ', '.join(map(str,ans)) + '>')