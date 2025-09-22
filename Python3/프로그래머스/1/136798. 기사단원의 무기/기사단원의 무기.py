def solution(number, limit, power):
    div_cnt = [0] * (number+1) # 각 정수에 대한 약수 카운트 배열
    for i in range(1, number+1): # i를 모든 배수 j의 약수로 기록
        for j in range(i, number+1, i):
            div_cnt[j] += 1

    result = 0
    for i in range(1, number+1):
        att = div_cnt[i] # i의 약수 개수
        if att > limit:
            att = power
        result += att
    return result