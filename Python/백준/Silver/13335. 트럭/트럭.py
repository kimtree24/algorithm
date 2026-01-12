import sys
from collections import deque
input = sys.stdin.readline

n, w, l = map(int, input().strip().split())
trucks = deque(map(int, input().strip().split()))

bridge = deque([0 for _ in range(w)])
cur_weight = 0
time = 0

while trucks or cur_weight > 0:
    time += 1
    
    out = bridge.popleft()
    cur_weight -= out
    
    if trucks and cur_weight + trucks[0] <= l:
        next_truck = trucks.popleft()
        bridge.append(next_truck)
        cur_weight += next_truck
    else:
        bridge.append(0)
print(time)