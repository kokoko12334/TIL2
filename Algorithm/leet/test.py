

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        Q = deque(senate)
        while len(Q) > 1:
            s = Q.popleft()
            try:
                Q.remove('R' if s == 'D' else 'D')
                Q.append(s)
            except ValueError:
                pass
        return "Dire" if Q.pop() == "D" else "Radiant"
    


a = Solution()

print(a.predictPartyVictory("DRRDRDRDRDDRDRDR"))