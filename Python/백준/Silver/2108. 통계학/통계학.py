import sys
from collections import Counter

n = int(sys.stdin.readline())
num_list = []
for i in range(n):
    num_list.append(int(sys.stdin.readline()))

print(round(sum(num_list) / n))

num_list.sort()

print(num_list[n // 2])


counter = Counter(num_list)
mode_freq = counter.most_common()
if len(mode_freq) > 1 and mode_freq[0][1] == mode_freq[1][1]:
    mode = mode_freq[1][0]
else:
    mode = mode_freq[0][0]
print(mode)

print(num_list[-1]-num_list[0])