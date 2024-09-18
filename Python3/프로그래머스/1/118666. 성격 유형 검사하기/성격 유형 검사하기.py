def solution(survey, choices):
    result = []
    for i in range(len(survey)):
        if choices[i] == 1:
            result.append(survey[i][0] + '3')
        elif choices[i] == 2:
            result.append(survey[i][0] + '2')
        elif choices[i] == 3:
            result.append(survey[i][0] + '1')
        elif choices[i] == 5:
            result.append(survey[i][1] + '1')
        elif choices[i] == 6:
            result.append(survey[i][1] + '2')
        elif choices[i] == 7:
            result.append(survey[i][1] + '3')
                 
    R = 0
    C = 0
    J = 0
    A = 0
    T = 0
    F = 0
    M = 0
    N = 0
    
    for i in range(len(result)):
        if result[i][0] == 'R':
            R += int(result[i][1])
        elif result[i][0] == 'C':
            C += int(result[i][1])
        elif result[i][0] == 'J':
            J += int(result[i][1])
        elif result[i][0] == 'A':
            A += int(result[i][1])
        elif result[i][0] == 'T':
            T += int(result[i][1])
        elif result[i][0] == 'F':
            F += int(result[i][1])
        elif result[i][0] == 'M':
            M += int(result[i][1])
        elif result[i][0] == 'N':
            N += int(result[i][1])

    ans = []
    if R >= T:
        ans.append('R')
    else:
        ans.append('T')
    
    if C >= F:
        ans.append('C')
    else:
        ans.append('F')
    
    if J >= M:
        ans.append('J')
    else:
        ans.append('M')
    
    if A >= N:
        ans.append('A')
    else:
        ans.append('N')
    
    
    return ''.join(ans)
    