
t = int(input())


dp = [0] * (1000001)

dp[1] = 1
dp[2] = 2
dp[3] = 4
s = 3
for _ in range(t):
    number = int(input())
    if number> s:
        for i in range(s+1,number+1):
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009
        s = number
        print(dp[number])
    else:
        print(dp[number])





