from collections import deque

def solution(book_time):
    # 방 q로 관리
    q_room = []
    # q의 최대 길이 트래킹
    q_max = 0
    
    # 소팅 -> 시작시간 순
    sorted_book_time = sorted(book_time, key = lambda x: x[0])
    
    for idx, time_set in enumerate(sorted_book_time):
        start_str = time_set[0]
        end_str = time_set[1]
        # 시간 문자열 파싱
        start_h, start_m = map(int,start_str.split(':'))
        end_h, end_m = map(int,end_str.split(':'))
        # 시간은 전부 분으로 치환
        start_to_min = start_h * 60 + start_m
        end_to_min = end_h * 60 + end_m
        
        q_room = [each_time for each_time in q_room if each_time[1] + 10 > start_to_min]
        
        # 지금 것 추가
        q_room.append([start_to_min, end_to_min])
        # 이번 텀 방 수
        this_room = len(q_room)
        
        # 가장 최대 방 수 트래킹
        q_max = max(q_max, this_room)
        
    return q_max
        
        
    
    