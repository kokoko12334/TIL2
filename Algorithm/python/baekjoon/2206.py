from collections import deque

#n: 세로 m: 가로
n, m  =[int(i) for i in input().split()]

lst = [input() for _ in range(n)]

que = deque([[0,0,0]])

seen = [[[0] * 2 for _ in range(m)] for _ in range(n)]
seen[0][0][0] = 1

dx = [1,0,-1,0]
dy = [0,1,0,-1]
flag = True

while que:
    y,x,z = que.popleft()
    if y == n-1 and x ==m-1:
        answer = seen[y][x][z]
        flag =False
        break
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if nx < 0 or nx>= m or ny <0 or ny >= n:
            continue
        
        v = lst[ny][nx]
        if not seen[ny][nx][z]:

            if v =="0":
                que.append([ny,nx,z])
                seen[ny][nx][z] = seen[y][x][z] +1

            if v == "1" and z ==0:
                que.append([ny,nx,z+1])
                seen[ny][nx][z+1] = seen[y][x][z] +1


if flag:
    print(-1)
else:
    print(answer)
