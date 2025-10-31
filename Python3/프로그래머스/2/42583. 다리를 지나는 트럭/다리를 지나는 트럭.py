from collections import deque
def solution(bridge_length, weight, truck_weights):
    cnt = 0
    truck_num = len(truck_weights)
    total_weight = 0
    delay_list = deque(truck_weights)
    on_bridge = deque([0 for _ in range(bridge_length)])
    clear = 0
    
    while clear < truck_num:
        # 끝나는 트럭
        out_truck = on_bridge.popleft()
        if out_truck != 0:
            clear += 1
            total_weight -= out_truck
        # 더 올라 갈 수 있는지 판단 -> 더 못올라감
        next_truck = 0
        if delay_list:
            next_truck = delay_list[0]
        if total_weight + next_truck > weight:
            cnt += 1
            on_bridge.append(0)
        # 더 올라가기 가능
        else:
            cnt += 1
            new_truck = 0
            if delay_list:
                new_truck = delay_list.popleft()
            on_bridge.append(new_truck)
            total_weight += new_truck
        
    return cnt