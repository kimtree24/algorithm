import sys

n = int(input())
time_list = list(map(int, sys.stdin.readline().rstrip().split()))

time_list.sort()
all_sum = 0
temp_sum = 0
for i in time_list:
    temp_sum += i
    all_sum += temp_sum
print(all_sum)