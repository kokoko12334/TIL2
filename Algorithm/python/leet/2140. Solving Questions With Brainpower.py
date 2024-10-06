from typing import List
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        n = len(questions)
        
        dp = [[0] * n for _ in range(2)]
        dp[1][-1] = questions[-1][0]

        for i in range(n-2, -1, -1):
            dp[0][i] = max(dp[1][i+1], dp[0][i+1])
            dp[1][i] = questions[i][0]
            i2 = questions[i][1] + i + 1
            if i2 < n:
                dp[1][i] += max(dp[1][i2], dp[0][i2]) 

        return max(dp[0][0], dp[1][0])
