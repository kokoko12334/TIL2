

# 행: 출발지 (A B C D E F 순)
# 열: 목적지 (A B C D E F 순)

INF = float("inf")
#방향 그래프
graph = [
    [0,7,12,INF,INF,INF],
    [INF,0,2,9,INF,INF],
    [INF,INF,0,INF,10,INF],
    [INF,INF,INF,0,INF,1],
    [INF,INF,INF,4,0,5],
    [INF,INF,INF,INF,INF,INF]
]

# #무방향
# graph = [
#     [0,7,12,INF,INF,INF],
#     [7,0,2,9,INF,INF],
#     [12,2,0,INF,10,INF],
#     [INF,9,INF,0,4,1],
#     [INF,INF,10,4,0,5],
#     [INF,INF,INF,1,5,0]
# ]

# 배열에서 가장 작은 값 찾는 함수
def get_smallest_value_index(distances,visited):

    min_value = INF
    
    min_value_index = 0
    
    for i in range(len(distances)):

        if not visited[i] and distances[i] < min_value : # 해당 노드를 방문하지 않고 최소값을 지닌 노드
            min_value = distances[i]
            min_value_index = i
    
    if min_value == INF: #모두 순회를 했는데 만약 최소값이 INF면 더이상 갈 곳이 없다는 뜻
        
        return -1
    
    else:

        return min_value_index



def dijkstra(start_node):
    visited = [False]*6 #방문노드 처리
    distances = graph[start_node][:] #시작노드의 거리 정보 가져오기
    visited[start_node] = True #시작노드를 방문처리
    
    while True:
        
        next_node = get_smallest_value_index(distances,visited) #다음 갈곳을 정한다.
        visited[next_node] = True #방문처리한다.

        if next_node == -1:  #더 이상 갈곳이 없으면 멈춘다.
            break
        
        cost = distances[next_node] #출발지에서 해당노드에 가기위한 비용을 가져온다.

        for i in range(len(distances)):
            
            if not visited[i]: 
                
                new_cost = cost + graph[next_node][i] #해당노드에 도달할때 비용 + 그 다음 노드에 갈 때 비용

                if new_cost < distances[i]: #테이블 값보다 작으면 업데이트
                    distances[i] = new_cost

    return distances           

# 예시로 0번 노드(A)에서 시작하는 다익스트라 알고리즘 실행
print(dijkstra(0))





##최적화


import heapq

INF = float("inf")

graph = [
    [0, 7, 12, INF, INF, INF],
    [INF, 0, 2, 9, INF, INF],
    [INF, INF, 0, INF, 10, INF],
    [INF, INF, INF, 0, INF, 1],
    [INF, INF, INF, 4, 0, 5],
    [INF, INF, INF, INF, INF, INF]
]

def dijkstra(start_node):
    visited = [False] * len(graph)  # 방문노드 처리
    distances = [INF] * len(graph)  # 거리 정보를 무한대로 초기화
    distances[start_node] = 0  # 시작 노드의 거리는 0으로 설정
    queue = []
    
    # 시작 노드를 우선순위 큐에 추가 (거리, 노드 인덱스)
    heapq.heappush(queue, (0, start_node))
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        # 이미 방문한 노드는 무시
        if visited[current_node]:
            continue
        
        visited[current_node] = True
        
        for neighbor in range(len(graph[current_node])):
            distance = graph[current_node][neighbor]
            if distance != INF and not visited[neighbor]:
                new_distance = current_distance + distance
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(queue, (new_distance, neighbor))
    
    return distances

# 예시로 0번 노드(A)에서 시작하는 다익스트라 알고리즘 실행
print(dijkstra(0))





