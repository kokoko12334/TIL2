
from bisect import bisect_left
class Solution:
    def increasingTriplet(self, nums) -> bool:
        
        lis = [nums[0]]

        for i in range(1, len(nums)):

            if lis[-1] < nums[i]:
                lis.append(nums[i])
            else:
                idx = bisect_left(lis,nums[i])
                lis[idx] = nums[i]
        
        length = len(lis)

        answer = True
        if length < 3:
            answer = False

        return answer