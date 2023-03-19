

n = int(input())


dp = [1,1,1,2,2,3] + ([0]*100)

front = 1
for i in range(6, len(dp)):
    dp[i] = dp[front] + dp[i-1]
    front += 1

for _ in range(n):
    num = int(input())
    print(dp[num-1])





