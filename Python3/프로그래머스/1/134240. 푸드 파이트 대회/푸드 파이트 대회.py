def solution(food):
    temp_result = []
    
    # 0 기준 전단
    for i in range(1,len(food)):
        use_food_num = food[i] // 2 # 사용할 수 있는 음식 수 (전단)
        temp_result.append(str(i) * use_food_num)
    
    left_str = ''.join(temp_result)
    return left_str + '0' + left_str[::-1]