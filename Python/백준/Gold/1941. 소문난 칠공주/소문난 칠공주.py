import sys
from collections import deque
input = sys.stdin.readline

grid = [list(input().strip()) for _ in range(5)]

def neighbors(idx):
    r, c = divmod(idx, 5)
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 5 and 0 <= nc < 5:
            yield nr*5 + nc

ans = 0
seen = set()

def dfs(picked, frontier, s_cnt):
    global ans
    remain = 7 - len(picked)
    if s_cnt + remain < 4:
        return

    if len(picked) == 7:
        fs = frozenset(picked)
        if fs in seen:
            return
        seen.add(fs)
        if s_cnt >= 4:
            ans += 1
        return

    for nxt in list(frontier):
        if nxt in picked:
            continue
        new_frontier = set(frontier)
        for nb in neighbors(nxt):
            new_frontier.add(nb)
        new_frontier.discard(nxt)
        for p in picked:
            new_frontier.discard(p)

        r, c = divmod(nxt, 5)
        dfs(picked | {nxt}, new_frontier, s_cnt + (1 if grid[r][c] == 'S' else 0))

for i in range(25):
    r, c = divmod(i, 5)
    dfs({i}, set(neighbors(i)), 1 if grid[r][c] == 'S' else 0)

print(ans)