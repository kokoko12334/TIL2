#16947번 문제 난이도 골드3
import sys
from collections import deque
sys.setrecursionlimit(10**8)

n=int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]
arr=[-1]*(n+1)

visited=[False]*(n+1)

#과거에 간 곳과 겹치면 안 됨

def dfs(last,now):
    global loop
    global loop_start
    global loop_end
    
    stack.append(now)
    visited[now]=True

    for node in graph[now]:
        if node!= last:
            if not visited[node]:
                dfs(now,node)
            else:
                loop=True
                loop_start=node
                loop_end=now
                return
        if loop:
            return
    stack.pop()
    
   
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

loop=False
loop_start=-1
loop_end=-1

stack=[]
L=[]
dfs(-1,1)

queue=deque()

while(1):
    x=stack.pop()
    queue.append(x)
    arr[x]=0
    if x==loop_start:
        break

#오잉? deque()로 print하는 경우 다르게 출력되네.

#힌트:dfs로 loop를 구한 다음에 bfs로 답을 낸다.

def bfs():
    while queue:
        x=queue.popleft()
        
        for node in graph[x]:
            if arr[node]==-1:
                queue.append(node)
                arr[node]=arr[x]+1

bfs()

print(" ".join(map(str,arr[1:])))