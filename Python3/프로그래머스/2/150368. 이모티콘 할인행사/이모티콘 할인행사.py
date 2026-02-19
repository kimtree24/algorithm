def make_emoticon_discount(emoticons):
    discount_list = [10,20,30,40]
    result = []
    m = len(emoticons)
    
    def dfs(idx, cur):
        if idx == m:
            result.append(cur[:])
            return
        for discount in discount_list:
            cur.append((emoticons[idx], discount))
            dfs(idx + 1, cur)
            cur.pop()
    dfs(0, [])
    return result
    

def buy(user, each_emoticon_discount, user_cnt, sum_money):
    money = 0 # 유저별 구매 금액
    buy_plus = False # 이모티콘 플러스 가입 여부
    
    # 이모티콘 별 계산
    for emoticon, discount in each_emoticon_discount:
        if user[0] <= discount:
            money += emoticon * (100 - discount) // 100
    # 이모티콘 플러스 가입 여부
    if user[1] <= money:
        buy_plus = True
        money = 0
    
    # 바깥 함수의 변수 변경
    if buy_plus:
        user_cnt[0] += 1
    sum_money[0] += money
    # 결과 리턴 [플러스 가입여부, 유저별 구매액]
    return [buy_plus, money]

def solution(users, emoticons):
    # 구현 문제
    # 이모티콘 플러스 서비스 가입 여부 및 가격 반환
    # 할인율 배열
    
    # 할인율 별 순환
    discount_isplus = [] # (플러스 유저 수, 이모티콘 구매액)
    emoticons_discount = make_emoticon_discount(emoticons)
    
    # 유저별 순환 -> 이거 돌면 전체 유저에 대한 결과
    isplus_list = []
    
    for each_emoticons_discount in emoticons_discount:
        user_cnt = [0]
        sum_money = [0]
        for user in users:
            isplus_money = buy(user, each_emoticons_discount, user_cnt, sum_money)
            isplus_list.append(isplus_money)
        
        discount_isplus.append((user_cnt[0], sum_money[0]))
    
    sorted_discount_isplus = sorted(discount_isplus, key = lambda x: (x[0], x[1]), reverse = True)
    return [sorted_discount_isplus[0][0], sorted_discount_isplus[0][1]]