class Solution(object):
    def findNumberOfLIS(self, nums):
        dp1, dp2 = [1] * len(nums), [1] * len(nums)
        count, maxval = 1, 1

        for i in range(1, len(nums)):
            
            for j in range(i):
                
                if nums[i] > nums[j]:
                    
                    if dp1[j] + 1 > dp1[i]:
                        dp1[i], dp2[i] = dp1[j] + 1, dp2[j]
                    elif dp1[j] + 1 == dp1[i]:
                        dp2[i] += dp2[j]

            if dp1[i] > maxval:
                maxval, count = dp1[i], dp2[i]
            elif dp1[i] == maxval:
                count += dp2[i]

        return count