from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        dp = [[0]*n for _ in range(n)]
        
        for i in range(n):
            dp[0][i] = matrix[0][i]

        for i in range(1,n):
            for j in range(n):
                v1 = float("inf")
                v2 = dp[i-1][j]
                v3 = float("inf")
                if j-1 >= 0:
                    v1 = dp[i-1][j-1]
                if j+1 < n:
                    v3 = dp[i-1][j+1]
                dp[i][j] = min(v1,v2,v3) + matrix[i][j]
        
        # for i in dp:
        #     print(i)

        return min(dp[-1])

        