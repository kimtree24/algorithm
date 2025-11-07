import math
def solution(players, m, k):
    # 시간별 서버 컴 개수
    time_slot = [0 for _ in range(24)]
    
    # 증설횟수
    result = 0
    
    # players 배열 돌면서 증설 여부 판단
    for time, player in enumerate(players):
        n = time_slot[time]
        if (n+1) * m > player:
            continue
        else:
            if player % m == 0:
                plus_num = player / m - n
            else:
                plus_num = math.ceil(player / m) - (n+1)
            for idx in range(time, time + k):
                if idx < 24:
                    time_slot[idx] += plus_num
            result += plus_num
    return result
        
    