n = int(input())
arr = [int(i) for i in input().split()]

dp = [[0] * n for _ in range(n)]

for i in range(0,n-1):
    s = i
    e = i + 1
    if arr[s] != arr[e]:
        dp[s][e] = 1

for gap in range(3, n+1):
    for i in range(0, n - gap + 1):
        s = i
        e = i + gap - 1
        if arr[s] == arr[e]:
            dp[s][e] = dp[s+1][e-1]
        else:
            dp[s][e] = min(dp[s+1][e], dp[s][e-1]) + 1

print(dp[s][n-1])



