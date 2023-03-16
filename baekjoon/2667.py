import sys
sys.setrecursionlimit(10**7)

n = int(input())
lst = []

for _ in range(n):
    lst.append(input())

##1인 지점만 찾기
graph = {}
for i in range(n):
    for j in range(n):
        if lst[i][j] == "1":
            s = str(i)+"."+str(j)
            graph[s] = []


####서로 연결된 곳 찾기
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for i in graph.keys():
    s = i.split(".")
    x = int(s[0])
    y = int(s[1])
    for j in range(4):
        nx = x +dx[j]
        ny = y +dy[j]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
        s2 = str(nx)+"."+str(ny)    
        if lst[nx][ny] == "1":
            graph[i].append(s2)        


seen = set()
stack = []
s = list(graph.keys())[0]
stack.append(s)
seen.add(s)
answer = []
cnt = 0
def dfs(cnt):
    if stack:
        s = stack.pop()
        
        cnt += 1
        for i in graph[s]:
            if i not in seen:
                stack.append(i)
                seen.add(i)   
        dfs(cnt)
    else:
        answer.append(cnt)
        cnt = 0
        remain = set(graph.keys()) - seen    
        if remain:
            s = list(remain)[0]
            stack.append(s)
            seen.add(s)
            
            dfs(cnt)

dfs(cnt)

answer = sorted(answer)
print(len(answer))
for i in answer:
    print(i)


