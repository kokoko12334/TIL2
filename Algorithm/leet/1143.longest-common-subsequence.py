class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n1 = len(text1)
        n2 = len(text2)
        #row:n1, col:n2
        dp = [[0]*n1 for _ in range(n2)]

        for i in range(n2):
            for j in range(n1):
                
                if text2[i] == text1[j]:
                    if i-1 >= 0 and j-1 >= 0:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                
        answer = dp[n2-1][n1-1]
        # for i in dp:
        #     for j in i:
        #         answer= max(answer,j)
        return answer
