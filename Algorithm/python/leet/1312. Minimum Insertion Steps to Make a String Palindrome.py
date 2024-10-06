class Solution:
    def minInsertions(self, s: str) -> int:
        
        n = len(s)
        s_r = s[::-1]
        dp = [[0]*(n+1) for _ in range(n+1)]
        maxx = 0
        
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == s_r[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                maxx = max(maxx, dp[i][j])
        
        return n - maxx