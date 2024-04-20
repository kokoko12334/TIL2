from collections import defaultdict
from typing import List

# 과반수라는 것이 확정되면 이를 이용할 수 있다. => 과반수 - (나머지) 해도 이는 양수가 나온다.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        cnt = 1
        m = nums[0]
        n = len(nums)
        for i in range(1,n):
            num = nums[i]
            if cnt == 0:
                m = num
                cnt = 1
            elif num == m:
                cnt += 1
            else:
                cnt -= 1
 
        return m