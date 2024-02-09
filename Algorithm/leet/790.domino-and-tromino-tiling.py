class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n==3:
            return 5
            
        dp = [0]*(n+1)
        mod = 10**9+7
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        for i in range(4,n+1):
            dp[i] = (dp[i-1]*2 + dp[i-3])%mod
        
        return dp[-1]