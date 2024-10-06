from collections import defaultdict
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        g = defaultdict(list)
        for c,p in prerequisites:
            g[c].append(p)

        seen = set()

        def dfs(c):
            if not g[c]:
                return True
            
            if c in seen:
                return False

            seen.add(c)

            for nextt in g[c]:
                if not dfs(nextt):
                    return False
            g[c] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True






