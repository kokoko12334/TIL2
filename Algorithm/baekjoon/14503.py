import sys

input = sys.stdin.readline

n, m = [int(i) for i in input().split()]
y, x, d = [int(i) for i in input().split()]
matrix = []
for _ in range(n):
    matrix.append([int(i) for i in input().split()])

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while True:
    matrix[y][x] = 2
    
    check = False # True이면 청소되지 않은 빈칸이 있는 경우 
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if matrix[ny][nx] == 0:
            check = True

    if check:
        d = (d-1)%4
        ny = y + dy[d]
        nx = x + dx[d]
        if matrix[ny][nx] == 0:
            y, x = ny, nx
        
    else:
        back = (d+2)%4
        ny = y + dy[back]
        nx = x + dx[back]
        if matrix[ny][nx] == 1:
            break
        else:
            y, x = ny, nx

answer = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            answer += 1

print(answer)