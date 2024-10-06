

n = int(input())

answer2 = 0
dp = [0]*(n+1)
dp[1] = 1
dp[2] = 1
def fib_dp(n):
    global answer2
    if n == 1 or n == 2:
        return dp[n]
    for i in range(3,n+1):
        answer2 += 1
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

fib_dp(n)
answer1 = [0]*(n+1)
answer1[1] = 1
answer1[2] = 1
for i in range(3,n+1):
    answer1[i] = answer1[i-1] + answer1[i-2]

print(answer1[-1], answer2)
