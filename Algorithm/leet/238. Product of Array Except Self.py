class Solution:
    def productExceptSelf(self, nums):


        n = len(nums)
        answer=[0]*n
        
        mul = 1
        for v in nums:
            mul *= v
        
        for i in range(n):
            if nums[i] != 0:
                answer[i] = mul//nums[i]
            else:
                arr = nums[:i] + nums[i+1:]
                result = 1
                for v in arr:
                    result *= v
                answer[i] = result
        
        return answer
    

a = Solution()
print(a.productExceptSelf([-1,1,0,-3,3]))
