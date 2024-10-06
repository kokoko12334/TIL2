from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        r = 0
        n = len(nums)
        current = nums[0]
        answer = float('inf')
        if current >= target:
            answer = 1
        length = 1
        while l <= r:
            # print("############################ ")
            # print(f"l:{l}, r:{r}, current:{current}")
            if current >= target:
                # print(f"{current} >= {target}")
                current -= nums[l]
                l += 1
                length -= 1
                
            else:
                # print(f"{current} < {target}")
                r += 1
                if r >= n:
                    break
                current += nums[r]
                length += 1
            # print(f"len:{length}, current:{current}, l,r:{l,r}")
            if current >= target:
                answer = min(length, answer)

        if answer == float('inf'):
            return 0

        return answer