from collections import deque

k = int(input())

w, h = [int(i) for i in input().split()]

grid = []
for _ in range(h):
    grid.append([int(i) for i in input().split()])


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

hy = [1, 2, 2, 1, -1, -2, -2, -1]
hx = [2, 1, -1, -2, -2, -1, 1, 2]

q = deque([(0, 0, 0, k)])

seen = [[[-1] * (k+1) for _ in range(w)] for _ in range(h)]
seen[0][0][k] = 0
while q:
    y, x, cnt, horse = q.popleft()

    if y == (h - 1) and x == (w - 1):
        break
    if horse > 0:
        for i in range(8):
            ny = hy[i] + y
            nx = hx[i] + x
            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue
            
            if grid[ny][nx] == 1 or seen[ny][nx][horse - 1] != -1:
                continue
            
            seen[ny][nx][horse - 1] = cnt + 1
            q.append((ny, nx, cnt + 1, horse - 1))

    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if nx < 0 or nx >= w or ny < 0 or ny >= h:
            continue
        if grid[ny][nx] == 1 or seen[ny][nx][horse] != -1:
            continue
        
        seen[ny][nx][horse] = cnt + 1
        q.append((ny, nx, cnt + 1, horse))


answer = 9999999999
for i in seen[h-1][w-1]:
    if i != -1:
        answer = min(answer, i)

if answer ==9999999999:
    print(-1)
else:
    print(answer)