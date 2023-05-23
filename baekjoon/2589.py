from collections import deque
import sys
input = sys.stdin.readline

n,m = [int(i) for i in input().split()]
#n: 세로, m:가로

lst = [input() for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
q = deque()
maxx = 0
for i in range(n):
    for j in range(m):
        if lst[i][j] == "W":
            continue
        q.append([i,j])
        seen = [[0]*m for _ in range(n)]
        while q:
            y,x = q.popleft()
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if nx < 0 or nx >= m or ny <0 or ny >=n or lst[ny][nx] == "W" or (ny == i and nx ==j):
                    continue
                
                if not seen[ny][nx]:
                    q.append([ny,nx])
                    seen[ny][nx] = seen[y][x] + 1
                    if seen[ny][nx] > maxx:
                        maxx = seen[ny][nx]
        

print(maxx)

