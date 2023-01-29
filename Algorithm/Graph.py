from collections import deque

graph = {}
graph[1] = [2,3,4]
graph[2] = [1,4,5]
graph[3] = [1,4,7]
graph[4] = [2,3,8]
graph[5] = [2,6]
graph[6] = [5]
graph[7] = [3]
graph[8] = [4]


######dfs
stack = deque()
seen = {}
#첫번째 정점
vertex = 1
stack.append(vertex)
seen[vertex] = True

def dfs():
    if stack:
        out = stack.pop()
        print(out)
        for i in graph[out]:
            if i not in seen:
                stack.append(i)
                seen[i] = True
                
                
        dfs()

dfs()



######bfs
que = deque()
seen = {}
#첫번째 정점
vertex = 1
que.append(vertex)
seen[vertex] = True

def bfs():
    if que:
        out = que.popleft()
        print(out)
        for i in graph[out]:
            if i not in seen:
                que.append(i)
                seen[i] = True
                
        bfs()

bfs()



1 in seen