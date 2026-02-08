import heapq

n = int(input())
problem = {}

max_heap = []
min_heap = []

for _ in range(n):
    p, l = map(int, input().split())
    problem[p] = l
    heapq.heappush(max_heap, (-l, -p))
    heapq.heappush(min_heap, (l, p))

m = int(input())

for _ in range(m):
    cmd = input().split()

    if cmd[0] == 'add':
        p, l = int(cmd[1]), int(cmd[2])
        problem[p] = l
        heapq.heappush(max_heap, (-l, -p))
        heapq.heappush(min_heap, (l, p))

    elif cmd[0] == 'recommend':
        if cmd[1] == '1':
            while True:
                l, p = max_heap[0]
                if problem.get(-p) == -l:
                    print(-p)
                    break
                heapq.heappop(max_heap)
        else:
            while True:
                l, p = min_heap[0]
                if problem.get(p) == l:
                    print(p)
                    break
                heapq.heappop(min_heap)

    elif cmd[0] == 'solved':
        p = int(cmd[1])
        del problem[p]