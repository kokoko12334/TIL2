from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [0] * n
        for i in range(n-2, -1, -1):
            l_idx = i + 1
            r_idx = i + nums[i] + 1
            # print(f"i:{i}, l:{l_idx}, r:{r_idx}")
            if l_idx == r_idx:
                arr[i] = float('inf')
            else:
                arr[i] = min(arr[l_idx:r_idx]) + 1
        
        return arr[0]