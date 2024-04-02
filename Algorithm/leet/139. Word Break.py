from typing import List
# i: 끝점 j는 시작점=> dp[j] 에서 True이고 해당 s[j:i]까지 존재한다면 가능
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        dp = [i==0 for i in range(n+1)]
        # print(dp)

        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        # print(dp)

        return dp[-1]