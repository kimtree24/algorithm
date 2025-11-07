import math
def get_a(target_array):
    result = target_array[0]
    for num in target_array[1:]:
        result = math.gcd(result,num)
    return result

def solution(arrayA, arrayB):
    c = get_a(arrayA)
    y = get_a(arrayB)
    # 첫번째 조건
    flag_1 = False
    for num in arrayB:
        if num % c == 0:
            flag_1 = True
            break
    if flag_1:
        temp_1 = 0
    else:
        temp_1 = c
    # 두번째 조건
    flag_2 = False
    for num in arrayA:
        if num % y == 0:
            flag_2 = True
            break
    if flag_2:
        temp_2 = 0
    else:
        temp_2 = y
    result = max(temp_1, temp_2)
        
    return result
    