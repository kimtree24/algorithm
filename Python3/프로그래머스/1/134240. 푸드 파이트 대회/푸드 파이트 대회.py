def solution(food):
    result = ""
    
    # 0 기준 전단
    for i in range(1,len(food)):
        use_food_num = food[i] // 2 # 사용할 수 있는 음식 수 (전단)
        for j in range(use_food_num):
            result += str(i)
            
    result += "0"
    
    #  0 기준 후단
    for i in result[-2::-1]:
        result += i
    return(result)