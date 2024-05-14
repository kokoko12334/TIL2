class Solution:
    def solve(self, n, dp):
        if n <= 1:
            return 1
        if dp[n] != -1:
            return dp[n]
        ans = 0
        for i in range(1, n + 1):
            ans += self.solve(i - 1, dp) * self.solve(n - i, dp)
        dp[n] = ans
        return dp[n]

    def numTrees(self, n):
        dp = [-1] * (n + 1)
        return self.solve(n, dp)