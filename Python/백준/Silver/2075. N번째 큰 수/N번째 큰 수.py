import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    for num in map(int, input().split()):
        if len(heap) < n:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
print(heap[0])
