from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort(key=lambda x : x[1], reverse=True)
        n = len(pairs)
        dp = [[0]*n for _ in range(n+1)] 
        dp[0] = [1]*n
        maxx = [1]*n
        for i in range(1,n+1):
            base = maxx[i-1]
            for j in range(i-1,n):
                dp[i][j] = base
                # print(f"base:{base}, idx:{i,j}")
                if pairs[i-1][0] > pairs[j][1]:
                    dp[i][j] += 1
                    maxx[j] = max(maxx[j], dp[i][j])
        
        # print(pairs)
        # for i in dp:
        #     print(i)
        return dp[-1][-1]