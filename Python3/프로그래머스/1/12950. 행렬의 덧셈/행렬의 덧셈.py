def solution(arr1, arr2):
    ans = []
    for i in range(len(arr1)):
        sub = []
        for j in range(len(arr1[i])):
            sub.append(arr1[i][j]+arr2[i][j])
        ans.append(sub)
    return ans