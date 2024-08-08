from collections import deque, defaultdict

def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    
    for i in range(len(roads)):
        s, e = roads[i]
        graph[s].append(e)
        graph[e].append(s)
    
    seen = [-1] * (n+1)
    q = deque([(destination, 0)])
    seen[destination] = 0
    
    while q:
        node, cnt = q.popleft()
        for next_node in graph[node]:
            if seen[next_node] == -1:
                q.append((next_node, cnt+1))
                seen[next_node] = cnt + 1
    
    answer = []
    for i in sources:
        answer.append(seen[i])
    
    return answer