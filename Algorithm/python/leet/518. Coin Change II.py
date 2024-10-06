from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                # print(i,coin, i -coin)
                dp[i] += dp[i - coin]
                
        # print(dp)
        return dp[amount]



a = Solution()
b = a.change(amount=4, coins=[1,2,3])
print(b)