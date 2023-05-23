import sys
input  = sys.stdin.readline
n,m = [int(i) for i in input().split()]
#n: 세로 m: 가로

lst = [[int(i) for i in input().split()]for _ in range(n)]
total = 0
for i in range(n):
    for j in range(m):
        if lst[i][j]:
            total += 1
q = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]

answer = 0
while True:
    answer += 1
    next = []
    q.append([0,0])
    visited = [[0]*m for _ in range(n)]
    while q:
        
        y,x = q.pop()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny <0 or ny>=n or nx < 0 or nx >=m:
                continue
            if not visited[ny][nx]:
                if lst[ny][nx]:
                    next.append([ny,nx])
                    visited[ny][nx] = 1
                else:
                    q.append([ny,nx])
                    visited[ny][nx] = 1
    for i in next:
        lst[i[0]][i[1]] = 0
        total -= 1
    
    
    if not total:
        break
print(answer)
print(len(next))