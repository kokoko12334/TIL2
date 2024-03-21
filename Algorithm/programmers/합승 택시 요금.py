from heapq import *
def solution(n, s, a, b, fares):

    answer = 0
    costs = [[0]*(n+1) for _ in range(n+1)]

    for i in fares:
        t,f,c = i
        costs[t][f] = c
        costs[f][t] = c
    def dijkstra(start_node):
        dis = [float('inf')]*(n+1)
        dis[start_node] = 0
        seen = [0]*(n+1)
        hq = []
        heappush(hq,(0,start_node))
        while hq:
            cost, node = heappop(hq)
            if seen[node]:
                continue
            seen[node] = 1

            for i in range(n+1):
                c = costs[node][i]
                if c != 0 and not seen[i]:
                    heappush(hq,(cost+c,i))
                    dis[i] = min(dis[i],cost+c)
        return dis

    a_d = dijkstra(a)
    b_d = dijkstra(b)
    s_d = dijkstra(s)
    answer = float('inf')
    for i in range(1,n+1):
        summ = a_d[i] + b_d[i] + s_d[i]
        answer = min(answer,summ)
    return answer