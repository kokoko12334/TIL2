import sys
input = sys.stdin.readline
t = int(input())



def dp(n,arr):
    
    dp = [[float("inf")]*(n+1) for _ in range(n+1)]
    sum_arr = [0] *(n+1)
    for i in range(1,n+1):
        dp[i][i] = 0
        sum_arr[i] = arr[i-1] + sum_arr[i-1]

    
    for d in range(1,n):
        
        for i in range(1,n):
            j = i + d
            if j > n:
                break
            
            for k in range(i,j):
                add = (dp[i][k] + dp[k+1][j] + sum_arr[j] - sum_arr[i-1]) 

                dp[i][j] = min(dp[i][j], add)

    return dp[1][n]
# sum_arr[j] - sum_arr[i-1] => dp[i][j] 만드는 총비용
# (dp[i][k] + dp[k+1][j]) => dp[i][k], dp[k+1][j] 는 각 최소비용 이때 dp[1][1] 같은 것은 비용이 0이다.


for _ in range(t):

    n = int(input())
    arr = [int(i) for i in input().split()]
    a = dp(n,arr)
    print(a)


