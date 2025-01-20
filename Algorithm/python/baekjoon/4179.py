import sys
from collections import deque

input = sys.stdin.readline

ROW, COL = [int(i) for i in input().split()]

grid = []
for _ in range(ROW):
    string = input().strip("\n")
    grid.append(list(string))


fire_grid = [[-1] * COL for _ in range(ROW)]
fire = []
for i in range(ROW):
    for j in range(COL):
        if grid[i][j] == "J":
            start = (i, j, 0)
            grid[i][j] = 0
        elif grid[i][j] == "F":
            fire.append((i, j, 0))
            grid[i][j] = -3
        elif grid[i][j] == "#":
            fire_grid[i][j] = -2
            grid[i][j] = -2
        else:
            grid[i][j] = -1

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
q = deque()

for i in fire:
    q.append((i))
    y, x, cnt = i
    fire_grid[y][x] = cnt
while q:
    y, x, cnt = q.popleft()
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if nx < 0 or nx >= COL or ny < 0 or ny >= ROW:
            continue
        if fire_grid[ny][nx] >= 0 or fire_grid[ny][nx] == -2:
            continue
        fire_grid[ny][nx] = cnt + 1
        q.append((ny, nx, cnt + 1))


q = deque()
q.append((start))
y, x, cnt = start
grid[y][x] = cnt
answer = float("inf")
while q:
    y, x, cnt = q.popleft()
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if nx < 0 or nx >= COL or ny < 0 or ny >= ROW:
            continue
        if (fire_grid[ny][nx] != -1 and cnt >= fire_grid[ny][nx] - 1) or grid[ny][nx] == -2 or grid[ny][nx] >= 0:
            continue
        grid[ny][nx] = cnt + 1
        q.append((ny, nx, cnt + 1))

# print("FIREEE")
# for i in fire_grid:
#     print(i)

# print("gird")
# for i in grid:
#     print(i)

answer = float("inf")
for i in range(COL):
    ele = grid[0][i]
    if ele >= 0:
        answer = min(ele, answer)

for i in range(COL):
    ele = grid[ROW - 1][i]
    if ele >= 0:
        answer = min(ele, answer)

for i in range(ROW):
    ele = grid[i][0]
    if ele >= 0:
        answer = min(ele, answer)

for i in range(ROW):
    ele = grid[i][COL - 1]
    if ele >= 0:
        answer = min(ele, answer)

if answer == float("inf"):
    print("IMPOSSIBLE")
else:
    print(answer + 1)