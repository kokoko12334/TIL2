from collections import deque
import sys
sys.setrecursionlimit(10**8)
#lst[h][n][m]  => [높이][세로][가로]
m, n , h = [int(i) for i in input().split()]

total = m*n*h
one = []
lst = []
time = []

for j in range(h):
    box = []
    time1 = []
    
    for k in range(n):

        lst2 = [int(i) for i in input().split()]
        box.append(lst2)
        
        for i in range(len(lst2)):
            if lst2[i] == 1:
                one.append([j,k,i])
                total -= 1
            elif lst2[i] == -1:
                total -= 1    
        time1.append([0]*m)
        
    lst.append(box)
    time.append(time1)


dx = [1,0,-1,0,0,0]     #가로
dy = [0,1,0,-1,0,0]     #세로
dz = [0,0,0,0,1,-1]     #높이



que = deque(one)

#lst[h][n][m]  => [높이][세로][가로]
maxday = 0
def bfs():
    global maxday
    global total
    if que:
        out = que.popleft()
        
        z = out[0]
        y = out[1]
        x = out[2]
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx>=m or ny <0 or ny >= n or nz < 0 or nz >= h:
                continue
            if lst[nz][ny][nx] == 0:
                lst[nz][ny][nx] = 1
                time[nz][ny][nx] = time[z][y][x] + 1
                if maxday < time[nz][ny][nx]:
                    maxday = time[nz][ny][nx]
                total -= 1    
                que.append([nz,ny,nx])
                
        bfs()

if total:
    bfs()


if total == 0:
    answer = maxday
else:
    answer = -1

print(answer)