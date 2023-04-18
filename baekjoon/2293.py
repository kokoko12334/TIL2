


n, k = [int(i) for i in input().split()]

coins = [int(input()) for _ in range(n)]
coins.sort()

dp = [0]*(k+1)
dp[0] = 1
for i in coins:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]

print(dp[k])
