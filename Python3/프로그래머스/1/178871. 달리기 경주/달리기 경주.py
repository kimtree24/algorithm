def solution(players, callings):
    dict_players = dict()
    
    for idx, player in enumerate(players):
        dict_players[player] = idx
    
    for player in callings:
        cur_idx = dict_players[player]
        before_idx = cur_idx - 1
        before_player = players[before_idx]
        
        temp = players[before_idx]
        players[before_idx] = players[cur_idx]
        players[cur_idx] = temp
        
        dict_players[player] = cur_idx - 1
        dict_players[before_player] = cur_idx
    return players
        
        
        
        
        