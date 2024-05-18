from collections import deque

def topological_sort(graph,vertex):

    entries = [0] * vertex
    for i in range(vertex):
        for v in graph[i]:
            entries[v] += 1

    q = deque()
    
    result = []
    for i in range(vertex):
        if not entries[i]:
            q.append(i)
    
    while q:
        node = q.popleft()
        result.append(node)
        for next_node in graph[node]:
            entries[next_node] -= 1
            if not entries[next_node]:
                q.append(next_node)
    
    return result

g = {
    0: [1,2],
    1: [5],
    2: [3,4],
    3: [5],
    4: [5],
    5: []
}

answer = topological_sort(g,6)
print(answer)