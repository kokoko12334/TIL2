import sys
input = sys.stdin.readline

n = int(input())

lst = [int(i) for i in input().split()]

dp = [[0]*21 for _ in range(n-1)]
dp[0][lst[0]] = 1


for i in range(n-2):
    for j in range(21):
        if dp[i][j]:
            n1 = j + lst[i+1]
            if n1 <= 20:
                dp[i+1][n1] += dp[i][j]
            n2 = j - lst[i+1]
            if n2 >= 0 :
                dp[i+1][n2] += dp[i][j]

print(dp[-1][lst[-1]])

