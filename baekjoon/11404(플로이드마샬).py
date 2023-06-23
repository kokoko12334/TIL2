import sys

### dp[i][j] = min(dp[i][j], dp[i][x] + dp[x][j])

input = sys.stdin.readline
n = int(input())
m = int(input())

dp = [[float("inf")]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            dp[i][j] = 0

for _ in range(m):
    i,j,c = [int(k) for k in input().split()]
    dp[i-1][j-1] = min(dp[i-1][j-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])


for i in range(n):
    for j in range(n):
        if dp[i][j] == float("inf"):
            dp[i][j] = 0

for i in dp:
    print(*i)





