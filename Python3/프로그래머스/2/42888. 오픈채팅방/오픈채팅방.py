def solution(record):
    # 최종 결과 저장용
    result = [''] * len(record)
    # 출입 관리 자료구조 {id : [(idx, 명령어)]}
    in_out_dict = {}
    
    # 최종 닉네임 관리 {id : nick}
    fi_nick = {}
    
    cnt = 0
    
    # record 파싱
    for idx, each_record in enumerate(record):
        # 명령어, 아이디, 닉네임
        splited_list = each_record.split(' ')
        order, user_id = splited_list[0], splited_list[1]
        # 명령어가 enter인 경우
        if order == 'Enter':
            nick = splited_list[2]
            fi_nick[user_id] = nick
            if not in_out_dict.get(user_id):
                in_out_dict[user_id] = []
            # 출입관리dict에 추가
            temp_set = (idx, order)
            in_out_dict[user_id].append(temp_set)
        if order == "Leave":
            # 출입관리dict에 추가
            temp_set = (idx, order)
            in_out_dict[user_id].append(temp_set)            
        # 명령어가 change인 경우
        if order == 'Change':
            nick = splited_list[2]
            fi_nick[user_id] = nick
            cnt += 1
    # 출입 관리 돌면서 각 유저별 판단
    for user_id, order_list in in_out_dict.items():
        # 최종 유저 닉네임
        user_nick = fi_nick[user_id]
        # 각 유저별 각 명령어
        for each_order in order_list:
            idx, order = each_order
            if order == 'Enter':
                result[idx] = f'{user_nick}님이 들어왔습니다.'
            else:
                result[idx] = f'{user_nick}님이 나갔습니다.'
    
    ans = []
    for r in result:
        if r:
            ans.append(r)
    return ans