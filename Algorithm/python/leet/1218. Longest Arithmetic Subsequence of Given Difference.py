from collections import defaultdict
from bisect import bisect_right
from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        dic = defaultdict(list)
        n = len(arr)
        for i in range(n):
            num = arr[i]
            dic[num].append(i)

        dp = [1] * n
        answer = 1
        for i in range(n):
            num = arr[i]
            target = num + difference
            subs = dic[target]
            if subs:
                idx = bisect_right(subs,i)
                sub = subs[idx:]
                for j in sub:
                    dp[j] = max(dp[i]+1, dp[j])
                    answer = max(answer, dp[j])
        
        return answer
    
# 뒤에서 부터 탐색
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        dp = defaultdict(int)
        n = len(arr)
        answer = 1
        for i in range(n-1,-1,-1):
            num = arr[i]
            target = num + difference
            if target in dp:
                dp[num] = dp[target] + 1
            else:
                dp[num] = 1
            answer = max(answer, dp[num])
        
        return answer