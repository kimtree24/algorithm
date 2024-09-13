def solution(n, arr1, arr2):
    result = []
    for i in range(n):
        map1 = bin(arr1[i])[2:].zfill(n)
        map2 = bin(arr2[i])[2:].zfill(n)
        temp = []
        for i in range(n):
            if map1[i] == '0' and map2[i] == '0':
                temp.append(' ')
            else:
                temp.append('#')
        reStr = ''.join(temp)
        result.append(reStr)
    return result
    