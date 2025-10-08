def solution(schedules, timelogs, startday):
    result = 0
    
    for sch_idx, timelog in enumerate(timelogs):
        ok_day = 0
        for idx, each_time in enumerate(timelog):
            day = (idx + startday) % 7
            if day == 6 or day == 0:
                ok_day += 1
                continue
            else:
                time_bound = (schedules[sch_idx] + 10)
                hour = time_bound // 100
                minute = time_bound % 100
                
                if minute >= 60:
                    time_bound = (hour + 1) * 100 + minute - 60
                    
                if each_time <= time_bound:
                    ok_day += 1
        if ok_day == 7:
            result += 1
    return result
                
                