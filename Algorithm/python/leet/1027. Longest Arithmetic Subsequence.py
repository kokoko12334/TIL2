from collections import defaultdict
from typing import List

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        n = len(nums)
        minn = min(nums)
        maxx = max(nums)
        a = maxx - minn
        answer = 0
        for dif in range(-a,a+1):
            dp = defaultdict(int)
            result = 0
            for i in range(n-1,-1,-1):
                num = nums[i]
                target = num + dif
                if target in dp:
                    dp[num] = dp[target] + 1
                else:
                    dp[num] = 1
                result = max(result, dp[num])
            answer = max(answer, result)

        return answer