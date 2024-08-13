
from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        answer = []
        operator = []
        n = len(expression)
        arr = []
        l = 0
        for i in range(n):
            if expression[i] in {"*", "-", "+"}:
                
                operator.append((i, expression[i]))
                arr.append(expression[l:i])
                arr.append(expression[i])
                l = i + 1
        arr.append(expression[l:i+1])
        
        return answer