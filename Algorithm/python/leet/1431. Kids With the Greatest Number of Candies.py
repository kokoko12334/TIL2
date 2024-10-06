class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        
        max_candies = max(candies)
        answer = []
        for i in candies:
            result = False
            if i + extraCandies >= max_candies:
                result = True
            answer.append(result)
        
        return answer