def solution(array, commands):
    
    result = []
    
    for command in commands:
        i, j, k = command
        target_array = array[i-1:j]
        target_array.sort()
        result.append(target_array[k-1])
        
    return result