import sys

input = sys.stdin.readline 

n = int(input())

arr = [[0]*n for _ in range(n)]

for i in range(n):
    matrix = [int(i) for i in input().split()]
    arr[i][i] = matrix


dp = [[float("inf")]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0


def cal(i,j,k,g):
    num1,num2 = arr[i][j]
    num2,num3 = arr[k][g]
    
    result = num1*num2*num3
    arr[i][g] = [num1,num3]

    return result

for d in range(1,n):
    for i in range(n-d):
        j = i + d
        for k in range(i,j):
            dp[i][j] = min(dp[i][j], (cal(i,k,k+1,j) + dp[i][k] + dp[k+1][j]))


for i in dp:
    print(i)

print(dp[0][n-1])

