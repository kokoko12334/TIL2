

# A B C D E F  


INF = float("inf")

#방향
# graph = [
#     [0,7,12,INF,INF,INF],
#     [INF,0,2,9,INF,INF],
#     [INF,INF,0,INF,10,INF],
#     [INF,INF,INF,0,INF,1],
#     [INF,INF,INF,4,0,5],
#     [INF,INF,INF,INF,INF,INF]
# ]


#무방향
graph = [
    [0,7,12,INF,INF,INF],
    [7,0,2,9,INF,INF],
    [12,2,0,INF,10,INF],
    [INF,9,INF,0,4,1],
    [INF,INF,10,4,0,5],
    [INF,INF,INF,1,5,0]
]








#가장 작은 값 찾기


def get_smallest_value_index(cost_list,visited):

    min_value = INF
    
    min_value_index = 0
    
    for i in range(len(cost_list)):

        if not visited[i] and cost_list[i] < min_value : # 해당 노드를 방문하지 않고 최소값을 지닌 노드
            min_value = cost_list[i]
            min_value_index = i
    
    if min_value == INF: #모두 순회를 했는데 만약 최소값이 INF면 더이상 갈 곳이 없다는 뜻
        
        return -1
    
    else:

        return min_value_index



def dijkstra(start_node):
    visited = [0]*6 #방문노드 처리
    cost_list = graph[start_node][:] #시작노드의 거리 정보 가져오기
    visited[start_node] = 1 #시작노드를 방문처리
    
    while True:
        
        next_node = get_smallest_value_index(cost_list,visited) #다음 갈곳을 정한다.
        visited[next_node] = 1 #방문처리한다.

        if next_node == -1:  #더 이상 갈곳이 없으면 멈춘다.
            break
        
        cost = cost_list[next_node] #출발지에서 해당노드에 가기위한 비용을 가져온다.

        for i in range(len(cost_list)):
            
            if not visited[i]: 
                
                new_cost = cost + graph[next_node][i] #해당노드에 도달할때 비용 + 그 다음 노드에 갈 때 비용

                if new_cost < cost_list[i]: #테이블 값보다 작으면 업데이트
                    cost_list[i] = new_cost

    return cost_list            




dijkstra(2)






















