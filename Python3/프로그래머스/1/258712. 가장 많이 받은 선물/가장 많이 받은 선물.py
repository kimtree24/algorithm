def solution(friends, gifts):
    len_friends = len(friends)
    # 이름별 인덱스 관리
    friend_idx = {friend: idx for idx, friend in enumerate(friends)}
    
    # 주고받은 선물 테이블 // gift_table[a][b] -> a가 b에게 준 선물
    gift_table = [[0 for i in range(len_friends)] for i in range(len_friends)]
    
    # 선물지수 관리
    gift_ratio = [0 for i in range(len_friends)]
    
    for each_gift in gifts:
        a, b = each_gift.split()
        a_idx, b_idx = friend_idx[a], friend_idx[b]
        
        # 선물지수 업데이트
        gift_ratio[a_idx] += 1 # 선물 주면 더하기
        gift_ratio[b_idx] -= 1 # 선물 받으면 빼기
        
        # 선물 테이블 업데이트
        gift_table[a_idx][b_idx] += 1
        
    # 내년도 판단
    next_gift = [0 for i in range(len_friends)]
    
    for i in range(len_friends):
        for j in range(i + 1, len_friends):
            if gift_table[i][j] > gift_table[j][i]:
                next_gift[i] += 1
            elif gift_table[i][j] < gift_table[j][i]:
                next_gift[j] += 1
            else:
                # 선물지수로 판단
                if gift_ratio[i] > gift_ratio[j]:
                    next_gift[i] += 1
                elif gift_ratio[i] < gift_ratio[j]:
                    next_gift[j] += 1
    return max(next_gift)