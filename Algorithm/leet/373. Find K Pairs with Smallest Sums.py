from heapq import *
from typing import List
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        hq = []
        n = len(nums2)
        m = len(nums1)
        for i in range(min(k,n)):
            heappush(hq,(nums1[0]+nums2[i],0,i))

        cnt = 0
        answer = []
        while hq and cnt < k:
            summ, i, j = heappop(hq)
            answer.append([nums1[i],nums2[j]])
            
            if i + 1 < m:
                heappush(hq,(nums1[i+1]+nums2[j],i+1,j))

            cnt += 1
        
        return  answer



        