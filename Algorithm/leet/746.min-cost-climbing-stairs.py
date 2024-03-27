class Solution:
    

    def minCostClimbingStairs(self, cost) -> int:
        

        n = len(cost)
        dp = [0]*n
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2,n):
            dp[i] = min(dp[i-1],dp[i-2]) +cost[i]
        
        return min(dp[-1],dp[-2])
    
        n = len(cost)
        dp = [0]*(n+2)
        # dp[1] = cost[0]

        for i in range(3,n+2):
            dp[i] = min(dp[i-1] + cost[i-2], dp[i-2] + cost[i-3])
  
        return dp[-1]
a = Solution()
a.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])