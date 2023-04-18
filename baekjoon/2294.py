
n, k = [int(i) for i in input().split()]

lst = [int(input()) for _ in range(n)]


dp = [99999]*(100001)


for i in lst:
    dp[i] = 1

for i in range(k+1):
    for j in range(i, k+1):
        dp[j] = min(dp[j], dp[j-i]+dp[i]) 
        


if dp[k] == 99999:
    print(-1)
else:
    print(dp[k])
