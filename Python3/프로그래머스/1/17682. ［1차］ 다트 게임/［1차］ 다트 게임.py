def solution(dartResult):
    scores = []
    i = 0
    n = len(dartResult)
    
    while i < n:
        if dartResult[i] == '1' and i + 1 < n and dartResult[i + 1] == '0':
            score = 10
            i += 2
        else:
            score = int(dartResult[i])
            i += 1
        
        bonus = dartResult[i]
        if bonus == "S":
            score = score
        elif bonus == "D":
            score = score ** 2
        elif bonus == "T":
            score = score ** 3
        i += 1
        
        if i < n and dartResult[i] in ['*', '#']:
            option = dartResult[i]
            if option == '*':
                score *= 2
                if scores:
                    scores[-1] *= 2
            elif option == '#':
                score *= -1
            i += 1
        scores.append(score)
        
    return sum(scores)
        
            
                
        
            
        
            