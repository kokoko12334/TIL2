

t = int(input())


for _ in range(t):
    n = int(input())
    lst = [[int(i) for i in input().split()] for _ in range(2)]

    dp = [[0]*n for _ in range(2)]

    
    if n >= 2:
        dp[0][0] = lst[0][0]
        dp[1][0] = lst[1][0]
        dp[1][1] = dp[0][0] + lst[1][1]
        dp[0][1] = dp[1][0] + lst[0][1]

        for j in range(2,n):
            dp[0][j] = max(dp[1][j-1], dp[1][j-2]) + lst[0][j]
            dp[1][j] = max(dp[0][j-1], dp[0][j-2]) + lst[1][j]

        print(max(dp[0][-1], dp[1][-1]))
    else:
        print(max(lst[0][0], lst[1][0]))












