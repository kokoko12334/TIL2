from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)

        dp = [[0]*n for _ in range(n)]
        dp[0][0] = 1
        for i in range(1,n):
            maxx = 0
            for j in range(i):
                dp[i][j] = dp[j][j]
                if nums[i] > nums[j]: 
                    dp[i][j] += 1
                maxx = max(maxx,dp[i][j])
            dp[i][i] = maxx
        for i in dp:
            print(i)
    
        
        return 0