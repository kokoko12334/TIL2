from collections import deque
import sys
input = sys.stdin.readline
#m:세로 n:가로
m,n,k = [int(i) for i in input().split()]
lst = [[0]*n for _ in range(m)]

for _ in range(k):
    y1,x1,y2,x2 = [int(i) for i in input().split()]
    for i in range(x1,x2):
        for j in range(y1,y2):
            lst[i][j] = 1

q = deque()
dx = [1,0,-1,0]
dy = [0,1,0,-1]
area = []
for i in range(m):
    for j in range(n):
        if not lst[i][j]:
            
            lst[i][j] = 1
            q.append([i,j])
            area.append(1)
            while q:
                out = q.popleft()
                y,x = out[0], out[1]
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if nx <0 or nx>=n or ny <0 or ny>=m:
                        continue
                    if not lst[ny][nx]:
                        q.append([ny,nx])
                        lst[ny][nx] = 1
                        area[-1] += 1
print(len(area))
print(*sorted(area))