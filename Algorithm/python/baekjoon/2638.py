from collections import deque
n, m = [int(i) for i in input().split()]

grid = []
for _ in range(n):
    grid.append([int(i) for i in input().split()])


def bfs():
    q = deque([(0, 0)])
    zeros = set()
    zeros.add((0, 0))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if grid[ny][nx]:
                continue

            if (ny, nx) in zeros:
                continue
            
            zeros.add((ny, nx))
            q.append((ny, nx))

    return zeros


chz = 0
for i in range(n):
    for j in range(m):
        if grid[i][j]:
            chz += 1

cnt = 0
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
all_set = set()
for i in range(n):
    for j in range(m):
        all_set.add((i, j))

while chz:

    zeros = bfs()
    ones = all_set - zeros

    remove_list = []
    for one in ones:
        y, x = one
        air = 0
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if grid[ny][nx] == 0 and (ny, nx) in zeros:
                air += 1
        
        if air >= 2:
            remove_list.append((y, x))
    
    for i in remove_list:
        y, x = i
        grid[y][x] = 0
        chz -= 1
    cnt += 1

print(cnt)