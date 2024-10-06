import sys
from collections import deque
sys.setrecursionlimit(10**7)
n,m, start_vertex = [int(i) for i in sys.stdin.readline().split()]


graph = {}
for i in range(1,n+1):
    graph[i] = []

for _ in range(m):
    k, v = [int(i) for i in sys.stdin.readline().split()]
    graph[k].append(v)
    graph[v].append(k)


for k,v in graph.items():
    graph[k] = sorted(v)

##dfs
seen = {}
stack = []
stack.append(start_vertex)
seen[start_vertex] = True
answer = []
def dfs():
    if stack:
        out = stack.pop()
        answer.append(out)
        for i in graph[out]:
            if i not in seen:
                stack.append(i)
                seen[i] = True
                dfs()


dfs()
print(*answer)



#bfs
seen = {}
que = deque()
que.append(start_vertex)
seen[start_vertex] = True
answer = []
def bfs():
    if que:
        out = que.popleft()
        answer.append(out)
        for i in graph[out]:
            if i not in seen:
                que.append(i)
                seen[i] = True
        bfs()
bfs()

print(*answer)

