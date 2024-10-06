class Solution:
    def bulbSwitch(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        return int(n**(1/2))
        