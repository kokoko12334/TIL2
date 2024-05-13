from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        dp = [[0]*(n+1) for _ in range(4)]
        
        dp[0][0] = -float("inf")
        dp[3][0] = -float("inf")
        
        dp[0][1] = -prices[0]
        dp[3][1] = -float("inf")
        answer = 0
        #0: 사고 1: 안사고, 2: 팔고, 3: 안팔고
        # 사고 = max(이전이전 안팔고, 이전 안사고) - 해당가격
        # 안사고 = max(이전 안사고, 이전 팔고)
        # 팔고 = max(이전 안팔고, 이전 사고 ) + 해당가격
        # 안팔고 = max(이전 안팔고, 이전 사고)
        for i in range(2, n+1):
            dp[0][i] = max(dp[2][i-2], dp[1][i-1]) - prices[i-1]
            dp[1][i] = max(dp[1][i-1], dp[2][i-1])
            dp[2][i] = max(dp[0][i-1], dp[3][i-1]) + prices[i-1]
            dp[3][i] = max(dp[0][i-1], dp[3][i-1])
            answer = max(answer, dp[0][i], dp[1][i], dp[2][i], dp[3][i])

        return answer