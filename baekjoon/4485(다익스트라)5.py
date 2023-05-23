from heapq import *
import sys
input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]
num = 1
while True:
    n = int(input())
    if not n:
        break
    lst = [[int(i) for i in input().split()]for _ in range(n)]
    dp = [[float("inf")]*n for _ in range(n)]
    dp[0][0] = lst[0][0]
    hq = []
    heappush(hq, [lst[0][0],0,0])
    
    while hq:
        d,y,x = heappop(hq)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx <0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            cost = d + lst[ny][nx] 

            if cost < dp[ny][nx]:
                dp[ny][nx] = cost
                heappush(hq, [cost,ny,nx]) 

    print("Problem {0}: {1}".format(num,dp[n-1][n-1]))
    num += 1