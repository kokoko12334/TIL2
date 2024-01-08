
# class Solution:
#     def moveZeroes(self, nums) -> None:
        
#         l = 0
#         r = 0
#         n = len(nums)
#         zeros = []
#         for i in range(n):
#             if nums[i] == 0:
#                 zeros.append(i)
        
#         for idx in zeros:

#             while idx < n:
                

#         return 0
    
class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1
a = Solution()

a.moveZeroes(nums = [0,1,0,3,12])
# a.moveZeroes(nums = [0,0,2,3,0,32,0,2,1,0])