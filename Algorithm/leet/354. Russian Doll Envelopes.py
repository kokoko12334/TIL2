from collections import defaultdict
from heapq import *
from bisect import bisect_left
from typing import List
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        n = len(envelopes)

        envelopes.sort(key = lambda x: x[1])
        dic = defaultdict(list)

        for i in range(n):
            w, h = envelopes[i]
            hq = dic[h]
            heappush(hq,w)
            dic[h] = hq

        lis = [0]
        for v in dic.values():
            num = heappop(v)
            if lis[-1] < num:
                lis.append(num)
            else:
                idx = bisect_left(lis,num)
                print(f"idx:{idx}, num:{num}")
                lis[idx] = num
        
        print(lis)

        return len(lis) - 1