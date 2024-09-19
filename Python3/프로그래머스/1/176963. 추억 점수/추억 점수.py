def solution(name, yearning, photo):
    ans = []
    for i in range(len(photo)):
        temp = 0
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                idx = name.index(photo[i][j])
                temp += yearning[idx]
        ans.append(temp)
    return ans