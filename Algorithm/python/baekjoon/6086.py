from collections import deque

def bfs(capacity, flow, source, sink, parent):
    visited = [False] * len(capacity)
    queue = deque([source])
    visited[source] = True
    
    while queue:
        current = queue.popleft()
        for next_node in range(len(capacity)):
            if not visited[next_node] and capacity[current][next_node] - flow[current][next_node] > 0:
                queue.append(next_node)
                visited[next_node] = True
                parent[next_node] = current
                if next_node == sink:
                    return True
    return False

def edmonds_karp(capacity, source, sink):
    n = len(capacity)
    flow = [[0] * n for _ in range(n)]
    parent = [-1] * n
    max_flow = 0
    
    while bfs(capacity, flow, source, sink, parent):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s] - flow[parent[s]][s])
            s = parent[s]
        
        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = parent[v]
        
        max_flow += path_flow
    
    return max_flow

n = int(input())

alphabet_mapping = {chr(i + 65): i for i in range(26)}  # 대문자 A-Z
alphabet_mapping.update({chr(i + 97): i + 26 for i in range(26)})  # 소문자 a-z는 26~51

capacity = [[0] * 52 for _ in range(52)]
source = 0  
sink = 25  

for _ in range(n):
    a, b, c = input().split()
    from_ = alphabet_mapping[a]
    to = alphabet_mapping[b]
    c = int(c)
    capacity[from_][to] += c
    capacity[to][from_] += c


print(edmonds_karp(capacity, source, sink))