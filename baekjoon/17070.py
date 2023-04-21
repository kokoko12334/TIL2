import sys
sys.setrecursionlimit(10**6)
n = int(input())



lst = [[int(i) for i in input().split()] for _ in range(n)]

dp = [[[-1]*n for _ in range(n)]for _ in range(3)]

dx = [1,0,1]
dy = [0,1,1]

#0가로 1은 세로 2는 대각선
def dfs(y,x, stat):
    if y == n-1 and x == n-1:
        return 1
    
    if dp[stat][y][x] != -1:
        return dp[stat][y][x]


    dp[stat][y][x] = 0

    if stat == 0:
        for i in [0,2]:
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx>=n or ny <0 or ny>=n:
                continue
            if i <= 1 and lst[ny][nx] == 0:
                dp[stat][y][x] += dfs(ny, nx,i)
        
            elif i == 2 and lst[ny][nx] == 0 and lst[y][nx] ==0 and lst[ny][x] == 0:
                dp[stat][y][x] += dfs(ny, nx, i)

    elif stat == 1:
        for i in [1,2]:
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx>=n or ny <0 or ny>=n:
                continue
            if i <= 1 and lst[ny][nx] == 0:
                dp[stat][y][x] += dfs(ny, nx,i)
        
            elif i == 2 and lst[ny][nx] == 0 and lst[y][nx] ==0 and lst[ny][x] == 0:
                dp[stat][y][x] += dfs(ny, nx,i)

    else:
        for i in range(3):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx>=n or ny <0 or ny>=n:
                continue
            if i <= 1 and lst[ny][nx] == 0:
               dp[stat][y][x]+= dfs(ny, nx,i)

            elif i == 2 and lst[ny][nx] == 0 and lst[y][nx] ==0 and lst[ny][x] == 0:
               dp[stat][y][x] += dfs(ny, nx,i)

    return dp[stat][y][x]

        

print(dfs(0,1,0))
