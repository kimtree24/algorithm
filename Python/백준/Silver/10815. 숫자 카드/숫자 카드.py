import sys
input = sys.stdin.readline

n = int(input().strip())
n_list = set(map(int, input().strip().split()))
m = int(input().strip())
m_list = map(int, input().strip().split())

result = []

for each_m in m_list:
    if each_m in n_list:
        result.append(1)
    else:
        result.append(0)
print(*result)