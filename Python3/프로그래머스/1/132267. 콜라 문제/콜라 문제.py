def solution(a, b, n):
    
    cur_bot = n # 지금 가지고 있는 빈 병
    
    result = 0 # 교환해서 받은 빈 병
    
    # 지금 가지고 있는 빈 병이 교환 가능한 최소 개수보다 큰 경우 계속 실행
    while cur_bot >= a:
        new_bot = (cur_bot // a) * b # 이번 교환으로 새로 받을 수 있는 콜라
        result += new_bot # 새로 받은 만큼 add
        cur_bot = cur_bot % a + new_bot # 지금 가진 병 갱신
    
    return result