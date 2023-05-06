
n = int(input())
lst = []
for _ in range(n):
    lst.append([int(i) for i in input().split()])


lst.sort(key = lambda x: x[0])



lst2 = []
for i in range(n):
    lst2.append(lst[i][1])

dp = [1]*(n)
dp[0] = 1
for i in range(1,n):
    for j in range(i):
        
        if lst2[i] > lst2[j]:
            dp[i] = max(dp[i], dp[j]+1)


print(n - max(dp))


