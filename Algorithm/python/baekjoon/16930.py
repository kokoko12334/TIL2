import sys
from collections import deque
input = sys.stdin.readline

n, m, k = [int(i) for i in input().split()]

matrix = []
for _ in range(n):
    arr = input().strip()
    matrix.append(arr)

x1, y1, x2, y2 = [int(i) for i in input().split()]

s = (x1-1, y1-1, 0)
dx = [1,0,-1,0]
dy = [0,1,0,-1]

seen = [[-1]*m for _ in range(n)]
seen[s[0]][s[1]] = 0

q = deque([s])
while q:
    y, x, cnt = q.popleft()

    for i in range(4):
        for j in range(1, k+1):
            ny = (dy[i] * j) + y
            nx = (dx[i] * j) + x
            if 0 > nx or nx >= m or ny < 0 or ny >= n:
                break
            if matrix[ny][nx] == "#":
                break
            if seen[ny][nx] == -1:
                seen[ny][nx] = cnt + 1
                q.append((ny, nx, cnt+1))
            if seen[ny][nx] <= seen[y][x]:
                break

# for i in seen:
#     print(i)

print(seen[x2-1][y2-1])