def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    for p in puddles:
        j, i = [num -1 for num in p]
        dp[i][j] = -1
    dp[0][0] = 1
    for dif in range(1, m+n-1):
        for i in range(max(dif-m+1, 0), min(dif+1, n)):
            j = dif - i
            if dp[i][j] == -1:
                continue
            cnt = 0
            
            if (0 <= j-1 < m) and dp[i][j-1] != -1:
                cnt += dp[i][j-1]
            if (0 <= i-1 < n) and dp[i-1][j] != -1:
                cnt += dp[i-1][j]
            dp[i][j] += cnt%1000000007
            
    return dp[-1][-1]