from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = days[-1]

        dp = [[0] *(n+1) for _ in range(4)]

        dp[0][1] = float('inf')
        if days[0] == 1:
            dp[1][1] = costs[0]
        dp[2][1] = costs[1]
        dp[3][1] = costs[2]

        sett = set(days)
        for i in range(2, n+1):
            
            day7 = max(1, i-6)
            day30 = max(1, i-29)
            dp[0][i] = min(dp[2][day7], dp[3][day30])

            minn = min(dp[1][i-1], dp[0][i-1])
            dp[1][i] = minn
            if i in sett:
                dp[1][i] += costs[0]

            dp[2][i] = minn + costs[1]
            dp[3][i] = minn + costs[2]

        answer = float('inf')
        for i in range(4):
            answer = min(dp[i][-1], answer)

        return answer