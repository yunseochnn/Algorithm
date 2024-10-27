def solution(N, stages):
    l = []
    total_players = len(stages)
    
    for i in range(1, N + 1): 
        cnt = stages.count(i)
        
        if total_players == 0:
            failure_rate = 0
        else:
            failure_rate = cnt / total_players
        
        l.append((i, failure_rate))
        total_players -= cnt

    sorted_l = sorted(l, key=lambda x: x[1], reverse=True)
    result = [item[0] for item in sorted_l]
    return result
