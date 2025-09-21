import heapq

def solution(k, score):
    heap = [] # 명예의 전당 (최소 힙)
    result = []

    for s in score:
        if len(heap) < k:
            heapq.heappush(heap, s) # 그대로 넣기
        else:
            if heap[0] < s: # 최소값보다 크면 교체
                heapq.heapreplace(heap, s)
        result.append(heap[0])
    return result