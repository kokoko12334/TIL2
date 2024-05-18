from collections import defaultdict, deque
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        entries = [0] * numCourses

        for order in prerequisites:
            c, pre = order
            graph[pre].append(c)
            entries[c] += 1

        q = deque()
        for i in range(numCourses):
            if not entries[i]:
                q.append(i)
        
        answer = []
        while q:
            c = q.popleft()
            answer.append(c)
            for next_c in graph[c]:
                entries[next_c] -= 1
                if not entries[next_c]:
                    q.append(next_c)

        if sum(entries):
            return []
        
        return answer
