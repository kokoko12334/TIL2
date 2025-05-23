from collections import deque

def bfs(capacity, flow, source, sink, parent):
    """BFS를 이용해 경로를 찾습니다."""
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
    """에드몬드-카프 알고리즘으로 최대 유량을 계산합니다."""
    n = len(capacity)
    flow = [[0] * n for _ in range(n)]
    parent = [-1] * n
    max_flow = 0
    
    while bfs(capacity, flow, source, sink, parent):
        # 현재 경로의 최소 잔여 용량(유량)
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s] - flow[parent[s]][s])
            s = parent[s]
        
        # 경로에 유량 추가
        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = parent[v]
        
        max_flow += path_flow
    
    return max_flow

# 사용 예제
if __name__ == "__main__":
    # 노드 수는 6이고, capacity[i][j]는 i에서 j로 가는 용량을 나타냅니다.
    # S:0, A:1, B:2, C:3, D:4, T:5
    capacity = [
        [0, 10, 0, 5, 0, 0],
        [0, 0, 4, 0, 8, 0],
        [0, 0, 0, 0, 0, 10],
        [0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 10],
        [0, 0, 0, 0, 0, 0]
    ]
    source = 0  # 시작점
    sink = 5    # 도착점
    
    print("최대 유량:", edmonds_karp(capacity, source, sink))
