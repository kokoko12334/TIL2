from heapq import *
from collections import defaultdict
def solution(n, paths, gates, summits):
    INF = float("inf")
    g = defaultdict(list)
        
    summits_sorted = sorted(summits)
    summits = set(summits)
    gates = set(gates)
    
    for path in paths:
        num1, num2, cost = path
        if num1 in summits:
            g[num2].append((num1, cost))
        elif num2 in summits:
            g[num1].append((num2, cost))
        elif num1 in gates:
            g[num1].append((num2, cost))
        elif num2 in gates:
            g[num2].append((num1, cost))
        else:
            g[num1].append((num2, cost))
            g[num2].append((num1, cost))
    
    costs = [INF] * (n+1)
    q = []
    for gate in gates:
        costs[gate] = 0
        heappush(q, (0,gate))
        
    while q:
        now_cost, node = heappop(q)
            
        if costs[node] < now_cost:
            continue
            
        for tup in g[node]:
            num, cost = tup
            new_cost = max(now_cost, cost)
            if new_cost < costs[num]:
                costs[num] = new_cost
                if num in summits:
                    continue
                heappush(q, (new_cost, num))
    # print(f"배열:{costs}")
        
    value = INF
    min_summit = 0
    for summit in summits_sorted:
        if value > costs[summit]:
            min_summit = summit
            value = costs[summit]
            
    return [min_summit,value]
    