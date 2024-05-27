from heapq import *
from collections import deque
from typing import List
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        # [profit,captial]
        n = len(profits)
        arr = []
        for i in range(n):
            arr.append((profits[i],capital[i]))
        arr = deque(sorted(arr, key = lambda x : x[1]))
        q = []
        while k:
            # print(arr)
            while arr and arr[0][1] <= w:
                p,_ = arr.popleft()
                heappush(q, -p)
            # print(f"{k}번째, hq:{q}")
            if q:
                profit = -heappop(q)
                # print(f"이득:{profit}")
                w += profit
                k -= 1
            else:
                break
        
        return w