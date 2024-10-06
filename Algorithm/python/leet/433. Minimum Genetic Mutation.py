from collections import deque
from typing import List
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        

        q = deque()
        q.append((startGene,0))
        seen = set()
        seen.add(startGene)
        while q:
            s, answer = q.popleft()
            
            if s == endGene:
                break
            for m in bank:
                
                if m not in seen:
                    cnt = 0
                    for i in range(8):
                        if s[i] != m[i]:
                            cnt += 1
                    if cnt == 1:
                        q.append((m,answer + 1))
                        seen.add(m)
                        
        if endGene not in seen:
            return -1

        return answer