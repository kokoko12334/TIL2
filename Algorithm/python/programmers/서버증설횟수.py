from collections import defaultdict, deque
def solution(players, m, k):
    answer = 0
    
    player_time_map = defaultdict(int)
    
    n = 0
    left = 0
    right = 0
    while left <= 1000 or right <= 1000:
        left = n * m
        right = (n + 1) * m
        
        for i in range(left, right):
            player_time_map[i] = n
        n += 1
    
    servers = deque()
    server_cnt = 0
    for i in range(24):
        
        for j in range(len(servers)):
            servers[j] -= 1
        
        while servers and servers[0] == 0:
            servers.popleft()
            server_cnt -= 1

        player_cnt = players[i]
        need_server_cnt = player_time_map[player_cnt]
        
        if need_server_cnt <= server_cnt:
            continue
        else:
            add_cnt = need_server_cnt - server_cnt
            for _ in range(add_cnt):
                servers.append(k)
                server_cnt += 1
                answer += 1

    return answer