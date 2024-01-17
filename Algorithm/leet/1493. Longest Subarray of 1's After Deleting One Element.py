from collections import deque
class Solution:
    def longestSubarray(self, nums) -> int:




        size = 0
        start = 0
        n = len(nums)
        dele = deque()
        k = 1
        answer = 0
        for i in range(n):
            
            if nums[i] == 1:
                size += 1
            else:
                if k > 0:
                    size += 1
                    k -= 1
                    dele.append(i)
                else:
                    
                    idx = dele.popleft()
                    size -= (idx - start + 1)
                    start = idx + 1
                    dele.append(i)
                    size += 1

            answer = max(answer, size)

        return answer - 1
    
a = Solution()
print(a.longestSubarray(nums =[0,1,1,1,0,1,1,0,1]))