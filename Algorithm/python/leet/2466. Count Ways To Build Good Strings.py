class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[zero] += 1
        dp[one] += 1
        div = 10**9 + 7
        for i in range(high + 1):
            if i + zero < high + 1:
                dp[i + zero] += dp[i]
            if i + one < high + 1:
                dp[i + one] += dp[i]
        
        return sum(dp[low:high+1]) % div