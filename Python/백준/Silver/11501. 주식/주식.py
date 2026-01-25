import sys

input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    p_list = list(map(int, input().strip().split()))
    p_list.reverse()

    max_p = 0
    buy_list = []
    result = 0

    for e_p in p_list:
        if e_p > max_p:
            # 이전 거 다 판매
            for each_sell in buy_list:
                result += (max_p - each_sell)
            # 새로운 최고 값 갱신
            max_p = e_p
            # buy_list 초기화
            buy_list = []
        else:
            buy_list.append(e_p)
    if buy_list:
        for each_sell in buy_list:
            result += (max_p - each_sell)
    print(result)