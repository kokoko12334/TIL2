from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = (n*(n+1))/2
        summ = 0
        for i in range(n):
            summ += nums[i]

        return int(expected_sum - summ) 