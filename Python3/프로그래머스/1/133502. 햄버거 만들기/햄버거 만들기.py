def solution(ingredient):
    ans = 0
    cur_ing = []
    last_ing = 0
    for i in ingredient:
        cur_ing.append(i)
        if i == 1:
            if last_ing == 3 and cur_ing[-4:] == [1,2,3,1]:
                ans += 1
                del cur_ing[-4:]
            last_ing = 1
        elif i == 2:
            last_ing = 2
        elif i == 3:
            last_ing = 3
    return ans