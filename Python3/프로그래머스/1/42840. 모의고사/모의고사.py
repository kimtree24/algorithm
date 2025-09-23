def solution(answers):
    _1 = [1,2,3,4,5]
    _2 = [2,1,2,3,2,4,2,5]
    _3 = [3,3,1,1,2,2,4,4,5,5]

    ans_num = {1:0, 2:0, 3:0}

    for i, ans in enumerate(answers):
        if ans == _1[i % len(_1)]:
            ans_num[1] += 1
        if ans == _2[i % len(_2)]:
            ans_num[2] += 1
        if ans == _3[i % len(_3)]:
            ans_num[3] += 1

    max_value = max(ans_num.values())

    return [k for k, v in ans_num.items() if v == max_value]