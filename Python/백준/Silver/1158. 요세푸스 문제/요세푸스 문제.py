import sys

input = sys.stdin.readline

n, k = map(int, input().strip().split())

num_list = [num for num in range(1, n + 1)]
pops = []
point = 0
while num_list:
    pop_idx = (point + (k - 1)) % len(num_list)
    pop_num = num_list.pop(pop_idx)
    point = pop_idx
    pops.append(pop_num)

print("<"+", ".join(map(str,pops))+">")