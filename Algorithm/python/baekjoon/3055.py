from collections import deque
import sys

input = sys.stdin.readline

n,m = [int(i) for i in input().split()]

mapp = [[i for i in input()] for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def flood(water):
    next = []
    seen = [[0]*m for _ in range(n)]
    for i in water:
        y,x = i
        seen[y][x] = 1

    for i in water:
        y,x = i
        for j in range(4):
            ny = y + dy[j]
            nx = x + dx[j]
            if nx < 0 or nx>=m or ny < 0 or ny>=n:
                continue
            if not seen[ny][nx] and mapp[ny][nx] == ".":
                mapp[ny][nx] = "*"
                next.append([ny,nx])
                seen[ny][nx] = 1
    return next



visited = [[-1]*m for _ in range(n)]
water = []
for i in range(n):
    for j in range(m):
        if mapp[i][j] == "*":
            water.append([i,j])
        elif mapp[i][j] == "S":
            start = [i,j,1]
            visited[i][j] = 0


q = deque()
q.append(start)
answer = 0
cnt = 0
while True:
    water = flood(water)
    cnt += 1
    while q:
        if q[0][2] != cnt:
            break
        y,x,d = q.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx>=m or ny < 0 or ny>=n:
                continue
            if visited[ny][nx] == -1:
                if mapp[ny][nx] == ".":
                    visited[ny][nx] = d
                    q.append([ny,nx,d+1])
                elif mapp[ny][nx] == "D":
                    answer = d
                    q = []
                    break 
    if not q:
        break

if answer:
    print(answer)
else:
    print("KAKTUS")
