

n, k = [int(i) for i in input().split()]


dp = [[1]*(n+1) for _ in range(k)]

for i in range(1,k):
    for j in range(1,n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(dp[-1][-1]%1000000000)