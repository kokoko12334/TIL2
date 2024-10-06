
n = int(input())

tree = []
dp = []
for _ in range(n):
    lst = [int(i) for i in input().split()]
    tree.append(lst)
    dp.append([0]*len(lst))


dp[0][0] = tree[0][0]

for i in range(1, n):
    row = len(tree[i])
    dp[i][0] = dp[i-1][0] + tree[i][0]
    dp[i][-1] = dp[i-1][-1] + tree[i][-1]
    for j in range(1, row - 1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + tree[i][j]
        
print(max(dp[-1]))