def solution(data, ext, val_ext, sort_by):
    temp_ext = []
    
    for i in range(len(data)):
        code = data[i][0]
        date = data[i][1]
        maximum = data[i][2]
        remain = data[i][3]
        
        
        if ext == 'code' and code < val_ext:
            temp_ext.append(data[i])
        elif ext == 'date' and date < val_ext:
            temp_ext.append(data[i])
        elif ext == 'maximum' and maximum < val_ext:
            temp_ext.append(data[i])
        elif ext == 'remain' and remain < val_ext:
            temp_ext.append(data[i])
        
    if sort_by == 'code':
        temp_ext.sort()
        return temp_ext
    
    elif sort_by == 'date':
        for i in range(len(temp_ext)):
            temp = temp_ext[i][0]
            temp_ext[i][0] = temp_ext[i][1]
            temp_ext[i][1] = temp
        temp_ext.sort()
        for i in range(len(temp_ext)):
            temp = temp_ext[i][0]
            temp_ext[i][0] = temp_ext[i][1]
            temp_ext[i][1] = temp
        return temp_ext
    
    elif sort_by == 'maximum':
        for i in range(len(temp_ext)):
            temp = temp_ext[i][0]
            temp_ext[i][0] = temp_ext[i][2]
            temp_ext[i][2] = temp
        temp_ext.sort()
        for i in range(len(temp_ext)):
            temp = temp_ext[i][0]
            temp_ext[i][0] = temp_ext[i][2]
            temp_ext[i][2] = temp
        return temp_ext
    
    elif sort_by == 'remain':
        for i in range(len(temp_ext)):
            temp = temp_ext[i][0]
            temp_ext[i][0] = temp_ext[i][3]
            temp_ext[i][3] = temp
        temp_ext.sort()
        for i in range(len(temp_ext)):
            temp = temp_ext[i][0]
            temp_ext[i][0] = temp_ext[i][3]
            temp_ext[i][3] = temp
        return temp_ext
            