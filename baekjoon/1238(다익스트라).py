from heapq import *
import sys
input = sys.stdin.readline
n,m,x = [int(i) for i in input().split()]

g = [[0]*n for _ in range(n)]

for _ in range(m):
    s,e,t = [int(i) for i in input().split()]
    g[s-1][e-1] = t

answer = [0]*n
for i in range(n):
    
    dp = [float("inf")]*n
    dp[i] = 0
    hq = []
    heappush(hq,[0,i])
    while hq:
        d,s = heappop(hq)
        if dp[s] < d:
            continue
        for j in range(n):
            if s == j or not g[s][j]:
                continue
            cost = g[s][j] + d
            if cost < dp[j]:
                dp[j] = cost
                heappush(hq, [cost,j])

    if i == x-1:
        for k in range(n):
            answer[k] += dp[k]
    else:
        answer[i] += dp[x-1]

print(max(answer))
    