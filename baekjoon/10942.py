import sys
input = sys.stdin.readline


n = int(input())

arr = [int(i) for i in input().split()]

dp = [[0]*(n) for _ in range(n)]

for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1


for i in range(n-2):
    for j in range(n-2-i):
        k = j + 2 +i
        
        if arr[j] == arr[k] and dp[j+1][k-1] == 1:
            dp[j][k] = 1

m = int(input())
for _ in range(m):
    y,x = [int(i) for i in input().split()]
    print(dp[y-1][x-1])

