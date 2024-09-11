from heapq import heappush, heappop
def solution(N, road, K):
    answer = 0
    
    g = [[float('inf')] * N for _ in range(N)]
    for i in range(N):
        g[i][i] = 0
        
    for i in range(len(road)):
        a, b, d = road[i]
        a -= 1
        b -= 1
        g[a][b] = min(g[a][b], d)
        g[b][a] = min(g[b][a], d)
    
    hq = []
    seen = [0] * N
    seen[0] = 1
    for i in range(N):
        dd = g[0][i]
        if dd != 0 and dd != float('inf'):
            heappush(hq, (dd, i))
    while hq:
        d, node = heappop(hq)
        if seen[node]:
            continue
        g[0][node] = d
        seen[node] = 1
        
        for i in range(N):
            dd = g[node][i]
            if dd != 0 and dd != float('inf'):
                if dd + d < g[0][i]:
                    heappush(hq, (dd+d, i))
    
    answer = 0
    for i in range(N):
        num = g[0][i]
        if num <= K:
            answer += 1
    return answer