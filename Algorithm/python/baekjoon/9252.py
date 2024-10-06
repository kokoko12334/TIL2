w1 = input()
w2 = input()

n1 = len(w1)
n2 = len(w2)

dp = [[0]*(n1+1) for _ in range(n2+1)]

str_w = [[""]*(n1+1) for _ in range(n2+1)]
for i in range(1,n2+1):
    for j in range(1,n1+1):

        if w1[j-1] == w2[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            str_w[i][j] = str_w[i-1][j-1] + w1[j-1]
            
        else:
            if dp[i-1][j] > dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
                str_w[i][j] = str_w[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
                str_w[i][j] = str_w[i][j-1]

print(dp[n2][n1])
print(str_w[n2][n1])