#팰린드롬 서브스트링을 먼저 확인하고 아니라면 이전에 dif값의 dp max로 정함
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        n = len(s)
        dp = [[0]*n for _ in range(n)]

        answer = 1
        for i in range(n):
            dp[i][i] = 1
            if i+1 < n:
                if s[i] == s[i+1]:
                    dp[i][i+1] = 2
                    answer = 2
                else:
                    dp[i][i+1] = 1
        
        for dif in range(2,n):
            for i in range(n-dif):
                j = i + dif
                # print(f"idx:{i,j}, dif:{dif}")
                if s[i] == s[j]:
                    dp[i][j] =  dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                answer = max(answer,dp[i][j])

        return answer
                

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        ans = 0

        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        for i in dp:
            print(i)
        return dp[0][-1]