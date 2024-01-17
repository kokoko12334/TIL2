n = int(input())
lst = [int(i) for i in input().split()]

dp = [0]* n
dp[0] = lst[0]

for i in range(1, n):
    
        maxx = 0
        for j in range(i):
            if lst[j] < lst[i] and dp[j] > maxx:
                
                maxx = dp[j]
        dp[i] = maxx + lst[i]

print(max(dp))
