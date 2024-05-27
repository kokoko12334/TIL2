from heapq import *
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        lst = []
        for i in nums:
            heappush(lst,(-i,i))
        
        
        for _ in range(k):
            _,v = heappop(lst)

        return v
        