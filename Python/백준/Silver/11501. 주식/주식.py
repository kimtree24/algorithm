import sys

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    p_list = list(map(int, input().strip().split()))

    max_p = 0
    result = 0

    for price in reversed(p_list):
        if price > max_p:
            max_p = price
        else:
            result += max_p - price
    print(result)