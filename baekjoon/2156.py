import sys
n = int(sys.stdin.readline())


lst = [int(sys.stdin.readline()) for _ in range(n)]
dp = [[0,0, 0] for _ in range(n)]

if n >= 2:
    dp[0][0] = lst[0]

    dp[1][0] = lst[0]+lst[1]
    dp[1][1] = lst[1]
    dp[1][2] = lst[0]
    
    for i in range(2, n):
        dp[i][0] = dp[i-1][1] +lst[i]
    

        dp[i][1] = max(dp[i-2]) + lst[i]
        
        dp[i][2] = max(dp[i-1])
       
    print(max(dp[-1]))
else:
    print(lst[0])


