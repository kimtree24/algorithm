def solution(video_len, pos, op_start, op_end, commands):
    posTime = int(pos[0:2]) * 60 + int(pos[3:])
    startTime = int(op_start[0:2]) * 60 + int(op_start[3:])
    endTime = int(op_end[0:2]) * 60 + int(op_end[3:])
    videoTime = int(video_len[0:2]) * 60 + int(video_len[3:])
    resultTime = 0
    
    for i in range(len(commands)):
        if startTime <= posTime <= endTime:
            posTime = endTime
        if commands[i] == 'prev':
            posTime = posTime - 10
            if posTime < 0:
                posTime = 0
            minute = posTime // 60
            second = posTime % 60
            if minute < 10:
                strMinute = '0'+str(minute)
            else:
                strMinute = str(minute)
            if second < 10:
                strSecond = '0'+str(second)
            else:
                strSecond = str(second)
            result = strMinute+':'+strSecond
            
        if commands[i] == 'next':
            posTime = posTime + 10
            if posTime > videoTime:
                posTime = videoTime
            minute = posTime // 60
            second = posTime % 60
            if minute < 10:
                strMinute = '0'+str(minute)
            else:
                strMinute = str(minute)
            if second < 10:
                strSecond = '0'+str(second)
            else:
                strSecond = str(second)
            result = strMinute+':'+strSecond
            
    resultTime = int(result[0:2]) * 60 + int(result[3:])
    if startTime <= resultTime <= endTime:
            resultTime = endTime
            minute = resultTime // 60
            second = resultTime % 60
            if minute < 10:
                strMinute = '0'+str(minute)
            else:
                strMinute = str(minute)
            if second < 10:
                strSecond = '0'+str(second)
            else:
                strSecond = str(second)
            result = strMinute+':'+strSecond
    return result