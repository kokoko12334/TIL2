import sys
from collections import deque
input = sys.stdin.readline
n, m = [int(i) for i in input().split()]

matrix = []
for _ in range(n):
    arr = input().strip()
    matrix.append(arr)

exit = (0,0)
namwoo = (0,0)
for i in range(n):
    for j in range(m):
        if matrix[i][j] == "N":
            namwoo = (i, j)
        elif matrix[i][j] == "D":
            exit = (i, j)

dy = [0,1,0,-1]
dx = [1,0,-1,0]
seen = [[0] * m for _ in range(n)]
q = deque()
q.append((exit[0], exit[1], 0))
ghost = -1
while q:
    y, x, cnt = q.popleft()
    if matrix[y][x] == "G":
        ghost = cnt
        break
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 > nx or nx >= m or 0 > ny or ny >= n:
            continue
        
        if not seen[ny][nx]:
            seen[ny][nx] = 1
            q.append((ny, nx, cnt+1))


seen = [[-1] * m for _ in range(n)]
q = deque()
q.append(namwoo)
seen[namwoo[0]][namwoo[1]] = 0
while q:
    y, x = q.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 > nx or nx >= m or 0 > ny or ny >= n:
            continue

        if seen[ny][nx] == -1:
            if matrix[ny][nx] == ".":
                seen[ny][nx] = seen[y][x] + 1
                q.append((ny, nx))
            elif matrix[ny][nx] == "D":
                seen[ny][nx] = seen[y][x] + 1
                q = []
                break

namwoo = seen[exit[0]][exit[1]]

if namwoo == -1 or (ghost != -1 and namwoo > ghost):
    print("No")
else:
    print("Yes")