from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the four states of profits
        # first_buy represents the profit after the first buy
        # first_sell represents the profit after the first sell
        # second_buy represents the profit after the second buy
        # second_sell represents the profit after the second sell
        first_buy, first_sell = -prices[0], 0
        second_buy, second_sell = -prices[0], 0
      
        # Loop through each price starting from the second price
        for price in prices[1:]:
            # Update first_buy to be either its previous value 
            # or the negative of the current price (representing a buy)
            first_buy = max(first_buy, -price)
          
            # Update first_sell to be either its previous value
            # or the sum of first_buy and the current price (representing a sell)
            first_sell = max(first_sell, first_buy + price)
          
            # Update second_buy to be either its previous value
            # or the difference of first_sell and the current price (representing a second buy)
            second_buy = max(second_buy, first_sell - price)
          
            # Update second_sell to be either its previous value
            # or the sum of second_buy and the current price (representing a second sell)
            second_sell = max(second_sell, second_buy + price)
      
        # The maximum profit after two transactions is located in second_sell,
        # and that's the result to return
        return second_sell