from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        comb = []
        k = 2*n
        def check(comb):
            stack = []
            for i in range(len(comb)):
                if comb[i] == "(":
                    stack.append(comb[i])
                else:
                    if stack and stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                
            if stack:
                return False

            return True

        def back():
            if len(comb) == k:
                if check(comb):
                    res.append("".join(comb))
                return 

            for b in ["(",")"]:
                comb.append(b)
                back()
                comb.pop()
        back()

        return res