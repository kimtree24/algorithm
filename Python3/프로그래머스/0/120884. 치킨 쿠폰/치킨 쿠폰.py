def solution(chicken):
    answer = 0
    
    # 재귀함수
    # rest_chicken : 발급받은 쿠폰으로 다시 시킬 수 있는 치킨
    # answer : 서비스 치킨
    def service_chicken(rest_chicken, answer):
        # 발급받은 쿠폰으로 다시 시킬 수 있는 치킨이 10 미만이면 쿠폰 발급 불가이므로 끝
        if rest_chicken < 10:
            return answer
        # 발급받은 쿠폰으로 다시 치킨 주문하고 서비스 치킨 카운팅
        elif rest_chicken >= 10:
            # 주문한 치킨으로 새로 발급받은 쿠폰
            new_coupon = int(rest_chicken / 10)
            
            # 쿠폰 발급 받은만큼 치킨 시킴
            answer += new_coupon
            
            # 치킨 시키고 남은 쿠폰은 적립
            new_coupon += rest_chicken % 10
            
            return service_chicken(new_coupon, answer)
    
    return service_chicken(chicken, answer)