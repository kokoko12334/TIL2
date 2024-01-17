
t = int(input())


def dp(n,arr):
    
    dp = [[0]*n for _ in range(n)]

    for j in range(n):
        for i in range(n):               
            lst = [dp[k][k+1] for k in range(i,j)]
            if lst:
                min_value = min(lst)
            else:
                min_value = 0
            dp[i][j] = sum(arr[i:j+1]) + min_value
    
    return dp[0][n-1]


def rec(i,j):
    
    if dp[i][j]:
        return dp[i][j]

    lst = [rec(k,k+1) for k in range(i,j)]
    return sum(arr[i:j+1]) + min(lst)
    


for _ in range(t):

    n = int(input())
    arr = [int(i) for i in input().split()]

    dp = [[0]*n for _ in range(n)]
    idx = 0
    for i in range(n):
        dp[idx+i][idx+i] = arr[idx+i]
        if idx+i+1 < n:
            dp[idx+i][idx+i+1] = sum(arr[idx+i:idx+i+2])

    print(rec(0,n-1))

