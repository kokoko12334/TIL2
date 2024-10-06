# dp[i][j] = > i ,j 까지의 최소합 s[i] == s[j] 면 전에꺼, 다르면 dp[i][j-1]+s[j], dp[i-1][j] + s[i] 중 최소
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        n = len(s1)
        m = len(s2)

        dp = [[0]*(1+m) for _ in range(n+1)]
        #s1: n = > y축  s2: m => x축

        for i in range(1, n+1):
            s = s1[i-1]
            dp[i][0] = dp[i-1][0] + ord(s)

        for i in range(1, m+1):
            s = s2[i-1]
            dp[0][i] = dp[0][i-1] + ord(s)
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    v1 = dp[i-1][j] + ord(s1[i-1])
                    v2 = dp[i][j-1] + ord(s2[j-1])
                    dp[i][j] = min(v1, v2)

        return dp[-1][-1]