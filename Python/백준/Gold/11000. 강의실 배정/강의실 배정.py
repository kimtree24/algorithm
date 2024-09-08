import sys
import heapq

n = int(sys.stdin.readline().rstrip())
time = []
for _ in range(n):
    s, t = map(int,sys.stdin.readline().rstrip().split())
    time.append([s,t])

time.sort()

room = []
heapq.heappush(room, time[0][1])

for i in range(1, n):
    if room[0] > time[i][0]:
        heapq.heappush(room, time[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, time[i][1])

print(len(room))
    