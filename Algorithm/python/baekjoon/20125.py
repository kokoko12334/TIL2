import sys

input = sys.stdin.readline
N = int(input())

matrix = []
for _ in range(N):
    matrix.append(list(input()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
heart = [0, 0]
for y in range(N):
    for x in range(N):
        if matrix[y][x] != "*":
            continue
        
        cnt = 0
        for i in range(4):
            
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if matrix[ny][nx] == "*":
                cnt += 1
        
        if cnt == 4:
            heart = [y, x]
            break        

answer = [0, 0, 0, 0, 0]
#왼쪽 팔
y = heart[0]
x = heart[1] - 1
while x >= 0 and matrix[y][x] == "*":
    answer[0] += 1
    x -= 1

#오른쪽 팔
y = heart[0]
x = heart[1] + 1
while x < N and matrix[y][x] == "*":
    answer[1] += 1
    x += 1

#허리
y = heart[0] + 1
x = heart[1]
while y < N and matrix[y][x] == "*":
    answer[2] += 1
    y += 1

#왼다리
leg_y = y
x = heart[1] - 1
while leg_y < N and matrix[leg_y][x] == "*":
    answer[3] += 1
    leg_y += 1
    
#오른다리
leg_y = y
x = heart[1] + 1
while leg_y < N and matrix[leg_y][x] == "*":
    answer[4] += 1
    leg_y += 1

print(heart[0] + 1, heart[1] + 1)
print(*answer)