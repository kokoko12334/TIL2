n = int(input())

dp = [0]* (n+1)
dp[0] = 1

if n>=2:
    dp[2] = 1

    for i in range(4,n+1, 2):

        if i%4 == 0:
            iter = i//4
            total = 0
            s = i-2
            dif = i-2
            for _ in range(iter):
                total += (dp[s] *dp[dif-s])

                s -= 2
            dp[i] = (total*2)%987654321
        else:
            iter = i//4
            total = 0
            s= i-2
            dif = i-2
            for _ in range(iter):
                total  += (dp[s] *dp[dif-s])

                s -= 2
            dp[i] = ((total*2) + dp[s]*dp[s])%987654321


print(dp[n])