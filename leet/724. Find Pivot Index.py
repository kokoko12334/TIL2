class Solution:
    def pivotIndex(self, nums) -> int:
        

        pivot = 0

        left = 0
        right = sum(nums[1:])
        answer = -1
        if left == right:
            answer = pivot
        
        else:
            for i in range(1, len(nums)-1):
                
                l_v = nums[pivot]
                r_v = nums[pivot+1]
                left += l_v
                right -= r_v
                if left == right:
                    answer = pivot+1
                    break
                pivot = i
            
            left = sum(nums[:-1])
            right = 0
            if left == right:
                answer = pivot+1
                
        return answer


a = Solution()
print(a.pivotIndex([-1,-1,0,1,1,0]))