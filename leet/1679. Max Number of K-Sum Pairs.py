class Solution:
    def maxOperations(self, nums, k: int) -> int:
        

        l = 0
        r = len(nums) - 1
        nums.sort()
        
        answer = 0
        while l < r:

            result = nums[l] + nums[r]

            if result > k:
                r -= 1
            elif result < k:
                l += 1
            else:
                answer += 1
                l += 1
                r -= 1

        return answer
    

a = Solution()

print(a.maxOperations(nums = [3,1,3,4,3], k = 6))