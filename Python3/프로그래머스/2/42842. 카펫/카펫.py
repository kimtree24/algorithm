def solution(brown, yellow):
    ans = []
    end = int(yellow ** 1/2)
    for i in range(1, yellow+1):
        if yellow % i == 0:
            y_row = yellow / i
            y_column = i
            
            b_row = y_row + 2
            b_column = y_column + 2
            
            if (b_row*b_column)-yellow == brown:
                ans.append(b_row)
                ans.append(b_column)
                break
    return ans