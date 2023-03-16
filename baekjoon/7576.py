import sys
from collections import deque
sys.setrecursionlimit(10**7)
#n 세로 길이 m은 가로 길이
m, n = [int(i) for i in sys.stdin.readline().split()]
box = []
for _ in range(n):
    row = [int(i) for i in sys.stdin.readline().split()]
    box.append(row)



dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

que = deque()
seen = set()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            string = str(i)+"."+str(j)
            que.append(string)
            seen.add(string)


max_day = 1
def bfs():
    global max_day
    if que:
        out = que.popleft()
        y, x = [int(i) for i in out.split(".")]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if nx < 0 or ny <0 or nx >= m or ny >=n:
                continue
            if box[ny][nx] == 0:
                box[ny][nx] = box[y][x] + 1
                
                string = str(ny) + '.'+ str(nx)    
                que.append(string)
                seen.add(string)
                if box[ny][nx] > max_day:
                    max_day = box[ny][nx]
        bfs()


bfs()

going = True
for i in range(n):
    if going:
        for j in range(m):
            if box[i][j] == 0:
                going = False
                break


if going:
    print(max_day - 1)
else:
    print(-1)    