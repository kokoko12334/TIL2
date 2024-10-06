from typing import List
from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:


        g = [[float("inf")]*n for _ in range(n)]

        for i in flights:
            f,t,p = i
            g[f][t] = p




        arr = [float("inf")]*n
        q = deque()
        q.append([0,0,src])
        while q:
            cost,cnt,node = q.popleft()
            for i in range(len(g[node])):
                n_cost = g[node][i]
                if cost != float("inf"):
                    nn = n_cost + cost
                    if nn < arr[i]:
                        arr[i] = nn
                        if cnt+1 <= k:
                            q.append([nn,cnt+1,i])



        answer = arr[dst]

        if answer == float("inf"):
            return -1
    

        return answer 