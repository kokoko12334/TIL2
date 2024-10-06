

n = int(input())

lst = [int(i) for i in input().split()]
dp = [0]*n

dp[0] = lst[0]
answer = dp[0]
for i in range(1, n):
    dp[i] = max(lst[i], dp[i-1] + lst[i])
    if dp[i] > answer:
        answer = dp[i]


                                    
print(answer)