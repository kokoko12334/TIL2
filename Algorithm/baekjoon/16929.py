n,m = [int(i) for i in input().split()]


g = []

for _ in range(n):
    g.append(input())


dx = [1,0,-1,0]
dy = [0,1,0,-1]
answer = False



def rec(s_y,s_x,y,x,cnt):
    global answer
    # print(f"시작:{s_y,s_x}   idx:{y,x}")
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        
        if cnt >= 4 and s_y == ny and s_x == nx:
            answer = True
            return
        
        if g[s_y][s_x] == g[ny][nx] and not seen[ny][nx]:
            seen[ny][nx] = 1
            rec(s_y,s_x,ny,nx,cnt+1)
            seen[ny][nx] = 0  # 해당 dfs가 끝나고 나면 해제 왜냐하면 후발주자가 사용할 수 있음.
 


flag = True
answer = False
for i in range(n):
    if flag:
        for j in range(m):
            seen = [[0]*m for _ in range(n)]
            seen[i][j] = 1
            rec(i,j,i,j,1)
            if answer:
                flag = False
                break
    
if answer:
    print("Yes")
else:
    print("No")


