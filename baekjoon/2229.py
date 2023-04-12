


n = int(input())

lst = [int(i) for i in input().split()]



dp = [[0]*n for _ in range(n)]


for i in range(n):
    for j in range(n):
        dp[i][j] = abs(lst[i]-lst[j])

print(10000*10000)