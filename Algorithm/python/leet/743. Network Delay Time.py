from heapq import heappush, heappop
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def dij(start):
 
            hq = []
            for i in range(1, n+1):
                if i == start or matrix[start][i] == INF:
                    continue
                
                heappush(hq, (matrix[start][i], i))

            dis = matrix[start]
            while hq:
                cost, node = heappop(hq)
                for i in range(1, n+1):
                    if matrix[node][i] + cost < dis[i]:
                        dis[i] = matrix[node][i] + cost
                        heappush(hq, (dis[i], i))
            return dis
        
        INF = float('inf')
        matrix = [[INF] * (n+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(n+1):
                if i == j:
                    matrix[i][j] = 0

        for t in times:
            u, v, w = t
            matrix[u][v] = w

        
        result = dij(k)
        
        answer = 0
        for r in result[1:]:
            if r == INF:
                return -1
            answer = max(answer, r)
        return answer
        