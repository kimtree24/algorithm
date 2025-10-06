def solution(ingredient):
    ans = 0
    cur_ing = []
    for i in ingredient:
        cur_ing.append(i)
        if len(cur_ing) >= 4 and cur_ing[-4:] == [1, 2, 3, 1]:
            del cur_ing[-4:]
            ans += 1
    return ans