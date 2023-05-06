import sys
input = sys.stdin.readline

n = int(input())

lst = [int(i) for i in input().split()]

dp = [1]* n 
di = {i:[lst[i]] for i in range(n)}

for i in range(1,n):
    idx = -1
    for j in range(i):
        if lst[i] > lst[j]:
            if dp[i] < dp[j] + 1:
                idx = j
            dp[i] = max(dp[i], dp[j] + 1)
    if idx != -1:
        di[i] = di[idx] + di[i]

maxx = max(dp)
maxx_idx = dp.index(maxx)
print(maxx)
print(*di[maxx_idx])

