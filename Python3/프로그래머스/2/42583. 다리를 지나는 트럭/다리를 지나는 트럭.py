from collections import deque

def solution(bridge_length, weight, truck_weights):
    t = 0
    waiting = deque(truck_weights)
    on_bridge = deque()
    curr_weight = 0

    while waiting or on_bridge:
        t += 1
        if on_bridge and on_bridge[0][1] == t:
            w, _ = on_bridge.popleft()
            curr_weight -= w
        if waiting and curr_weight + waiting[0] <= weight and len(on_bridge) < bridge_length:
            w = waiting.popleft()
            curr_weight += w
            on_bridge.append((w, t + bridge_length))

    return t