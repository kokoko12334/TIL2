import sys
sys.setrecursionlimit(10**6)
#m세로 n가로
m, n = [int(i) for i in input().split()]


lst = [[int(i) for i in input().split()]for _ in range(m)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


seen = [[-1] * n for _ in range(m)]

def dfs(y,x):
        
    if seen[y][x] != -1:
            return seen[y][x]
    
    if y == m-1 and x == n-1:
        return 1
    
    seen[y][x] = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if nx <0 or nx>=n or ny < 0 or ny>=m:
            continue
        
        if lst[ny][nx] < lst[y][x]:
            seen[y][x] += dfs(ny,nx)
    return seen[y][x]




print(dfs(0,0))





