
w1 = input()
w2 = input()

n1 = len(w1)
n2 = len(w2)

dp = [[0]*(n1+1) for _ in range(n2+1)]



for i in range(1,n2):
    for j in range(1,n1):
        if w2[i] > w1[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

for i in dp:
    print(i)


