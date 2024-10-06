def solution(matrix_sizes):
    n= len(matrix_sizes)
    m = matrix_sizes
    dp = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    
    for cnt in range(1, n+1):
        for i in range(n-cnt):
            j = i + cnt
            print(i,j)
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + (m[i][0] * m[k][1] * m[j][1]))

    return dp[0][-1]