from typing import List
from collections import deque
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        n = 201
        for i in strs:
            if n > len(i):
                n = len(i)
        answer = ""
        for i in range(n):
            ss = strs[0][i]
            
            for s in strs[1:]:
                if s[i] != ss:
                    return answer
            answer += ss
        return answer
    
