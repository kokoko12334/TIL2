
from collections import deque
class Solution:
    def longestOnes(self, nums, k: int) -> int:

        

        size = 0
        answer = 0
        start = 0
        flip = deque()
        for i in range(len(nums)):
            
            if nums[i] == 1:
                size += 1
            else:
                if k > 0:
                    size += 1
                    k -= 1
                    flip.append(i)
                else:
                    if flip:
                        idx = flip.popleft()

                        size -= (idx - start + 1) 
                        flip.append(i)
                        size += 1
                        start = idx + 1
                    else:
                        size = 0
            answer = max(size, answer)

        return answer
        

a = Solution()

print(a.longestOnes( nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))