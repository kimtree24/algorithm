import sys

n = int(input())
time_list = []
for i in range(n):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    time_set = [end, start]
    time_list.append(time_set)
time_list.sort()

time_Table = []
count = 0
end_time = 0

for i in range(n):
    start = time_list[i][1]
    end = time_list[i][0]
    if start >= end_time:
        time_Table.append([start, end])
        count +=1
        end_time = end

print(count)
