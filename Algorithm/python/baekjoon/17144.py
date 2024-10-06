import sys
input = sys.stdin.readline

r, c, t = [int(i) for i in input().split()]

matrix = []
for _ in range(r):
    matrix.append([int(i) for i in input().split()])

clean = []
for i in range(r):
    if matrix[i][0] == -1:
        clean.append([i, 0])

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def spread():
    new = [[0] * c for _ in range(r)]
    for idx in clean:
        y, x = idx
        new[y][x] = -1

    for y in range(r):
        for x in range(c):
            if not matrix[y][x] or matrix[y][x] == -1:
                continue
            num = matrix[y][x]//5
            cnt = 0
            for i in range(4):
                ny = dy[i] + y
                nx = dx[i] + x
                if nx < 0 or nx >= c or ny < 0 or ny >= r:
                    continue
                if matrix[ny][nx] == -1:
                    continue

                new[ny][nx] += num
                cnt += 1

            num2 = matrix[y][x] - (cnt*num)
            new[y][x] += num2
    
    return new

def turn_on():
    # 위의 공기청정기 = [a,0]
    # 뒤쪽 공기청정기 = [d,0]
    # [0][0] ~ [0][c-2] -> matrix[0][i] = matrix[0][i+1]
    # [1][0] ~ [a-1][0] -> matrix[i][0] = matrix[i-1][0]
    # [a][1] ~ [a][c-1] -> matrix[a][i] = matrix[a][i-1]
    # [0][c-1] ~ [a-1][c-1] -> matrix[i][c-1] = matrix[i+1][c-1]
    #[d][1] ~ [d][c-1] -> matrix[d][i] = matrix[d][i-1]
    #[d+1][c-1] ~ [r-1][c-1] -> matrix[i][c-1] = matrix[i-1][c-1]
    #[r-1][0] ~ [r-1][c-2] -> matrix[r-1][i] = matrix[r-1][i+1]
    #[d+1][0] ~ [r-2][0] -> matrix[i][0] = matrix[i+1][0]
    new = [arr[:] for arr in matrix]
    up = clean[0][0]
    down = clean[1][0]
    for idx in clean:
        y, x = idx
        new[y][x] = -1

    for i in range(c-1):
        new[0][i] = matrix[0][i+1]
    for i in range(1, up):
        new[i][0] = matrix[i-1][0]
    for i in range(1, c):
        new[up][i] = matrix[up][i-1] if matrix[up][i-1] != -1 else 0
    for i in range(up):
        new[i][c-1] = matrix[i+1][c-1]
        
    for i in range(1, c):
        new[down][i] = matrix[down][i-1] if matrix[up][i-1] != -1 else 0
    for i in range(down+1, r):
        new[i][c-1] = matrix[i-1][c-1]
    for i in range(c-1):
        new[r-1][i] = matrix[r-1][i+1]
    for i in range(down+1, r-1):
        new[i][0] = matrix[i+1][0]

    return new

for _ in range(t):
    matrix = spread()
    matrix = turn_on()

answer = 0
for i in range(r):
    for j in range(c):
        if not matrix[i][j] or matrix[i][j] == -1:
            continue
        answer += matrix[i][j]
print(answer)