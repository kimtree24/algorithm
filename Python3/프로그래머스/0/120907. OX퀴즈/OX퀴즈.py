def solution(quiz):
    
    answer = []
    
    for i in quiz: # 각 식 순회
        
        result = 0 # 검증할 전항 계산 값
        
        each_quiz = i.split(" ") # 판단할 식 분리
        
        for k in range(len(each_quiz)): # 각 인자별 판단
            # 문제 조건에 의해 index_error 가능성 없음
            if each_quiz[k] == "+":
                result = int(each_quiz[k-1]) + int(each_quiz[k+1])
            elif each_quiz[k] == "-":
                result = int(each_quiz[k-1]) - int(each_quiz[k+1])
            elif each_quiz[k] == "=":
                if result == int(each_quiz[k+1]):
                    answer.append("O")
                else:
                    answer.append("X")    
    return answer