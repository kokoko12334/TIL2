from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        share, rest = divmod(n+m,2)
        median_idx = share

        idx = 0
        p1 = 0
        p2 = 0
        arr = []
        while idx <= median_idx:
            num1 = 1111111
            num2 = 1111111
            if nums1 and p1 < n:
                num1 = nums1[p1]
            if nums2 and p2 < m:
                num2 = nums2[p2]

            if num1 <= num2:
                arr.append(num1)
                p1 += 1
                
            else:
                arr.append(num2)
                p2 += 1
            
            idx += 1

        # print(arr)

        if rest:
            return arr[-1]
        else:
            return (arr[-1] + arr[-2])/2








        




