import sys
input = sys.stdin.readline

n = int(input().strip())
p_list = sorted(map(int, input().strip().split()))

times = [0 for _ in range(n)]

for i in range(n):
    if i == 0:
        times[0] = p_list[0]
    else:
        times[i] = times[i - 1] + p_list[i]
print(sum(times))