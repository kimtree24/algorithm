def solution(progresses, speeds):
    done_day_list = []
    
    for idx, progress in enumerate(progresses):
        done_day = 0
        if ((100 - progress) % speeds[idx]) == 0:
            done_day = ((100 - progress) // speeds[idx])
        else:
            done_day = ((100 - progress) // speeds[idx]) + 1
        done_day_list.append(done_day)
    
    result = []
        
    current = done_day_list[0]
    count = 1

    for d in done_day_list[1:]:
        if d <= current:
            count += 1
        else:
            result.append(count)
            current = d
            count = 1

    result.append(count)
    return result
    
    
        
        