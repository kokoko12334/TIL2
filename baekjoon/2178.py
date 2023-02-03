from collections import deque
import sys
n,m = [int(i) for i in sys.stdin.readline().split()]


table = [list(sys.stdin.readline()) for _ in range(n)]
graph = {}
for i in range(n):
    for j in range(m):
        if table[i][j] == "1":
            graph[str(i)+str(j)] = []

for i in range(n):
    for j in range(m):
        if table[i][j] == '1':
            if i-1>=0 and table[i-1][j] == "1":    #upper
                graph[str(i)+str(j)].append(str(i-1)+str(j))
            if j-1>=0 and table[i][j-1] == "1":  #왼쪽
                graph[str(i)+str(j)].append(str(i)+str(j-1))
            if i+1<=n-1 and table[i+1][j] == "1":  #밑
                graph[str(i)+str(j)].append(str(i+1)+str(j))    
            if j+1<=m-1 and table[i][j+1] == "1":  #오른쪽
                graph[str(i)+str(j)].append(str(i)+str(j+1))



goal = str(n-1)+str(m-1)
seen = {}
que = deque()
que.append('00')
seen['00'] = True
answer = 1

while que:
    lst = []
    for _ in range(len(que)):
        out = que.popleft()

        for i in graph[out]:
            if i not in seen:
                lst.append(i)

                seen[i] = True
    que = deque(lst)
    answer += 1
    if goal in que:
        break    
print(answer)