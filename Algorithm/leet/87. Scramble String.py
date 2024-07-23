from collections import defaultdict
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        dp = defaultdict(list)

        def recur(s):
            if dp[s]:
                return dp[s]

            if len(s) == 1:
                return [s]
            
            arr = []
            for i in range(len(s)-1):
                ss1 = s[:i+1]
                ss2 = s[i+1:]
                re1 = recur(ss1)
                re2 = recur(ss2)
                arr.append((re1, re2))
            
            sett = set()
            for a in arr:
                b, c = a
                for i in b:
                    for j in c:
                        sett.add(i+j)
                        sett.add(j+i)
            
            dp[s] = sett

            return sett

        a = recur(s1)
        if s2 in a:
            return True

        return False