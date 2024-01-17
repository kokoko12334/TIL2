import sys


for _ in range(int(input())):
    num = int(input())
    dp = [0]*(num+1)
    if num>=4:
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4,num+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        print(dp[num])
    else:
        print(2**(num-1))
