def solution(a, b):
    # 1/31 -> 일
    # 2/1 -> 월
    day = ["FRI", "SAT", 'SUN', "MON", "TUE", "WED", "THU", "FRI"]
    day_cnt = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    total_day = 0
    
    for i in range(a - 1):
        total_day+= day_cnt[i]
    total_day += b - 1
    
    move_cnt = total_day % 7
    return(day[move_cnt])