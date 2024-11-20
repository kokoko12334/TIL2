import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

matrix = []
for _ in range(n):
    arr = [int(i) for i in input().split()]
    matrix.append(arr)


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
start = []
for y in range(n):
    for x in range(n):
        if matrix[y][x] != 1:
            continue
        for k in range(4):
            ny = dy[k] + y
            nx = dx[k] + x
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if matrix[ny][nx] == 0:
                start.append((y, x))
                break

one = []
for i in range(n):
    for j in range(n):
        if matrix[i][j]:
            one.append((i, j))

seen = [[0] * n for _ in range(n)]

cnt = 1
for i in one:
    y, x = i
    if seen[y][x] != 0:
        continue
    
    q = deque([(y,x)])
    seen[y][x] = cnt
    while q:
        y, x = q.popleft()

        for j in range(4):
            ny = dy[j] + y
            nx = dx[j] + x
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if matrix[ny][nx] and seen[ny][nx] == 0:
                seen[ny][nx] = cnt
                q.append((ny, nx))
    
    cnt += 1


answer = float('inf')

for nums in start:
    y, x = nums
    land = seen[y][x]
    q = deque([(y, x, land, 0)])
    # print(f"출발:{y,x} 시작섬:{land}")
    seen2 = set()
    seen2.add((y,x))
    while q:
        y, x, land, cnt = q.popleft()
        # print(f"y,x:{y,x}, 경로:{cnt}")
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if matrix[ny][nx] == 0:
                if (ny,nx) not in seen2:
                    q.append((ny, nx, land, cnt+1))
                    seen2.add((ny,nx))
            else:
                if seen[ny][nx] != land:
                    if answer > cnt:
                        answer = cnt
                        # print(ny,nx,cnt,land)

print(answer)
