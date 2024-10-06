from bisect import *
class Solution:
    def successfulPairs(self, spells, potions, success: int):
        n = len(potions)
        answer = []
        potions.sort()
        for s in spells:
            number = success/s
            idx = bisect_left(potions,number)
            
            cnt = n - idx
            answer.append(cnt)
        return answer