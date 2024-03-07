def solution(players, callings):
    # 선수:등수
    idx = {i : player for i, player in enumerate(players)}
    # 등수:선수
    p = {player : i for i, player in enumerate(players)}
    
    for i in callings:
        cur_location = p[i] # 현재 위치
        pre_location = cur_location-1 # 현재보다 앞에 있는 선수 등수
        pre_player = idx[pre_location]
        
        # 둥수:선수 에서 현재 등수의 선수를 앞 선수로 업
        idx[cur_location] = pre_player
        # 등수:선수 에서 앞 등수의 선수를 현재 선수로 다운
        idx[pre_location] = i
        
        # 선수:등수 에서 현재 선수의 등수를 앞 등수로 엎
        p[i] = pre_location
        # 선수:등수 에서 앞 선수의 등수를 현재 등수로 다운
        p[pre_player] = cur_location
        
    return list(idx.values())