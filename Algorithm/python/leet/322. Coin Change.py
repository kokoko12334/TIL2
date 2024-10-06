from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        dp = [float('inf')]*(amount)

        for coin in coins:
            if amount - coin >= 0:
                dp[amount-coin] = 1
        
        for i in range(amount-1,-1,-1):
            if dp[i] == float('inf'):
                continue
            for coin in coins:
                if i - coin >= 0:
                    dp[i-coin] = min(dp[i-coin], dp[i]+1)
                    
        if dp[0] == float('inf'):
            return -1
        
        return dp[0]