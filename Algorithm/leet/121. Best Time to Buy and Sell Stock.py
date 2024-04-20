from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*n for _ in range(3)]
        # dp[0]: 사기 dp[1]: 안사기 dp[2]: 팔기
        
        dp[0][0] = -prices[0]
        dp[1][0] = -99999999
        answer = 0
        for i in range(1,n):
            dp[0][i] = -prices[i]
            dp[1][i] = max(dp[0][i-1], dp[1][i-1])
            dp[2][i] = max(dp[0][i-1], dp[1][i-1]) + prices[i]
            answer = max(answer, dp[2][i])

        return answer
    

class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit