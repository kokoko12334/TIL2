from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        n = len(prices)
        profit = [0]*n
        buy = prices[0]
        
        
        for i in range(1,n):
            profit[i] = max(profit[i-1],prices[i]-buy-fee)
            buy = min(buy, prices[i]-profit[i])
            
        return profit[-1]




a = Solution()

a.maxProfit(prices = [1,3,2,8,4,9], fee = 2)

