import sys
sys.setrecursionlimit(10**6)
n = int(input())

lst = [[int(i) for i in input().split()]for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

dp = [[-1]*n for _ in range(n)]

def dfs(y,x):
    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        
        if lst[y][x] < lst[ny][nx]:
            dp[y][x] = max(dp[y][x], dfs(ny,nx) + 1)
            


    return dp[y][x]



for i in range(n):
    for j in range(n):
        dfs(i,j)


answer = 0
for i in range(n):
    for j in range(n):
        if dp[i][j] > answer:
            answer = dp[i][j]

print(answer+1)