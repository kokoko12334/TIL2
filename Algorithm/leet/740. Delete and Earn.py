from typing import List
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        n = max(nums)
        arr = [0] * (n+1)
        for num in nums:
            arr[num] += num
            
            
        dp = [[0]*(n+1) for _ in range(2)] 
        dp[0][1] = arr[1]
        dp[1][1] = arr[1]
        # print(arr)
        
        for i in range(2, n+1):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1])
            dp[1][i] = max(dp[0][i-2],dp[1][i-2]) + arr[i]

        # print(dp)

        return max(dp[0][-1], dp[1][-1])