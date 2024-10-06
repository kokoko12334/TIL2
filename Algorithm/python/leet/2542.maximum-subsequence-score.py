from heapq import *
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        hq = []
        n = len(nums2)
        for i in range(n):
            heappush(hq,(-nums2[i],i))
        print(hq)
        arr1 = []
        arr2 = []


        for _ in range(n):
            v, i = heappop(hq)
            arr2.append(-v)
            arr1.append(nums1[i])
        
        sum = 0
        hq2 = []
        answer = 0
        for i in range(n):
            v1 = arr1[i]
            v2 = arr2[i]

            heappush(hq2,(v1,v2))
            sum += v1
            if len(hq2) == k:
                answer = max(answer,sum*v2)
            if len(hq2) > k:
                min_v1,min_v2 = heappop(hq2)
                sum -= min_v1
                answer = max(answer,sum*v2)

        return answer
