from bisect import bisect_left
from typing import List
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        n = len(envelopes)
        envelopes.sort(key = lambda x: (x[0],-x[1]))

        lis = [envelopes[0][1]]
        
        for i in range(1, n):
            h = envelopes[i][1]
            if lis[-1] < h:
                lis.append(h)
            else:
                idx = bisect_left(lis, h)
                lis[idx] = h


        return len(lis)