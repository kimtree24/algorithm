def solution(bandage, health, attacks):
    do_time = bandage[0]
    heal = bandage[1]
    more_heal = bandage[2]
    
    max_health = health
    now_time = 0
    now_health = health
    success = 0
    i = 0
    while i < len(attacks):
        if attacks[i][0] > now_time:
            now_time += 1
            now_health += heal
            
            success += 1
            if success == do_time:
                now_health += more_heal
                success = 0
                
            if now_health > max_health:
                now_health = max_health
        
        else:
            now_time += 1
            now_health -= attacks[i][1]
            success = 0
            i += 1
            if now_health <=0:
                return -1
    return now_health
        