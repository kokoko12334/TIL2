import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
dy = [-2,-2,-1,-1,1,1,2,2]
dx = [-1,1,-2,2,-2,2,-1,1]
for _ in range(t):
    n = int(input())
    dp = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    sy,sx = [int(i) for i in input().split()]
    ey,ex = [int(i) for i in input().split()]
    q = deque([[sy,sx]])
    visited[sy][sx] = 1
    while q:
        y,x = q.popleft()
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx <0 or nx >= n or ny < 0 or ny>= n:
                continue
            if not visited[ny][nx]:
                dp[ny][nx] = dp[y][x] + 1
                visited[ny][nx] = 1
                q.append([ny,nx])
    print(dp[ey][ex])
    










