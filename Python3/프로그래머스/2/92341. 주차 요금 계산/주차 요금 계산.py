import math
from collections import defaultdict
# 시간 분으로 변환
def trans_time(time):
    return int(time[:2]) * 60 + int(time[3:])

# 각 기록별 정보 변환
def trans_each_record(each_record):
    split_record = each_record.split(' ')
    time_record = trans_time(split_record[0]) # 시간(분)
    car_number = split_record[1] # 차량번호
    info_record = split_record[2] # 출입여부
    trans_record = (time_record, car_number, info_record)
    return trans_record

# 계산 로직
def calculate(basic_time, basic_fee, unit_time, unit_fee, parking_time):
    # 주차 시간이 기본시간 안쪽인 경우
    if parking_time <= basic_time:
        return basic_fee
    # 주차 시간이 기본시간 초과인 경우
    else:
        # 기본시간 까지는 기본요금 부과
        parking_time -= basic_time
        return basic_fee + (math.ceil(parking_time / unit_time)) * unit_fee

def solution(fees, records):
    basic_time, basic_fee, unit_time, unit_fee = fees
    
    # 주차 기록 {car_number: (time_record)}
    car_in = {}
    # 차량별 시간 기록
    car_time = defaultdict(int)
    # 차량별 최종 결과 정리 {car_number: fee}
    car_result = defaultdict(int)
    
    for each_record in records:
        # 각 기록별 정보 정리
        time_record, car_number, info_record = trans_each_record(each_record)
        # info가 in인 경우
        if info_record == "IN":
            car_in[car_number] = time_record
        # 총 주차 시간 계산
        else:
            start = car_in.pop(car_number)
            car_time[car_number] += time_record - start
    # 출차 시간 없는 경우
    end_time = 23 * 60 + 59
    for car in car_in:
        car_time[car] += end_time - car_in[car]
    
    for car in car_time:
        each_result = calculate(basic_time, basic_fee, unit_time, unit_fee, car_time[car])
        car_result[car] = each_result
    sorted_car_result = list(sorted(car_result))
    ans = []
    for car in sorted_car_result:
        ans.append(car_result[car])
    return ans
        
            
        