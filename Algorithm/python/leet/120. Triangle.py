from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #j-1 >=0 j+1 <n => n은 행의 길이
        level = len(triangle)
        dp = [[float("inf")]*i for i in range(1,level+1)]

        dp[0][0] = triangle[0][0]
        
        for i in range(1,level):
            for j in range(i+1):
                v1 = float("inf")
                v2 = float("inf")
                if j-1 >= 0:
                    v1 = dp[i-1][j-1]
                if j <= i-1:
                    v2 = dp[i-1][j]
                # print(f"idx:{i,j}, v:{triangle[i][j]}, min:{min(v1,v2)}")
                dp[i][j] = min(v1,v2) + triangle[i][j]
        
        return min(dp[-1])