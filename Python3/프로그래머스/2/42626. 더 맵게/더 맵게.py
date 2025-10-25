import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while len(scoville) > 1:
        first = heapq.heappop(scoville)
        if first >= K:
            return cnt
        second = heapq.heappop(scoville)
        new = first + (second * 2)
        heapq.heappush(scoville, new)
        cnt += 1
    if scoville[0] >= K:
        return cnt
    else:
        return -1