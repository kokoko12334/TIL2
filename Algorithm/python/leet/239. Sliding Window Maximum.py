from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        q = deque()
        l = 0
        r = 0
        answers = []
        while r < n:
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if l > q[0]:
                q.popleft()
            if r+1 >= k:
                answers.append(nums[q[0]])
                l += 1
            r += 1
        return answers
