import sys
input = sys.stdin.readline

an, bn = map(int, input().strip().split())

a_list = list(map(int, input().strip().split()))
b_list = set(map(int, input().strip().split()))

result = []

for each_a in a_list:
    if each_a not in b_list:
        result.append(each_a)
result.sort()
print(len(result))
print(*result)