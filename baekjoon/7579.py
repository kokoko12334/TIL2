


n,m = [int(i) for i in input().split()]



memory = [int(i) for i in input().split()]
cost = [int(i) for i in input().split()]
nn = sum(cost)
dp = [[0]*(nn+1) for _ in range(n)]


for i in range(1, n):
    for j in range(1, nn+1):
        num1 = dp[i-1][j]
        num2 = dp[i-1][j-memory[j]] -cost[j]
        dp[i] = max(num1, num2)

