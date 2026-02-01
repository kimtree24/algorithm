import sys
from collections import defaultdict
from collections import Counter
input = sys.stdin.readline

m, n = map(int, input().strip().split())

rank_list = []

for _ in range(m):
    planets = list(map(int, input().strip().split()))
    sorted_planets = sorted(set(planets))
    rank = defaultdict(int)
    for i, each_univ in enumerate(sorted_planets):
        rank[each_univ] = i
    converse = []

    for each_planet in planets:
        converse.append(rank[each_planet])
    rank_list.append(tuple(converse))

counter = Counter(rank_list)
ans = 0
for k in counter.values():
    if k >= 2:
        ans += k * (k - 1) // 2
print(ans)