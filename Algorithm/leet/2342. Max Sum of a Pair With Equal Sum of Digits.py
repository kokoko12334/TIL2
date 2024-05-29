from collections import defaultdict
from typing import List
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        nums.sort(reverse = True)

        print(nums)
        dic = defaultdict(list)
        n = len(nums)
        for i in range(n):
            
            num = nums[i]
            result = 0
            while num:
                result += num%10
                num = num//10 
            
            dic[result].append(nums[i])
        
        answer = -1
        for v in dic.values():
            if len(v) < 2:
                continue
            answer = max(answer, v[0]+v[1])

        return answer

