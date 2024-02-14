
class Solution:
    def findPeakElement(self, nums) -> int:
        
        r = len(nums)
        l = 0
        n = len(nums)
        mid = (r-l)//2
        while True:
            
            v = nums[mid]
            if mid + 1 < n:
                v_right = nums[mid+1]
            else:
                v_right = -2147483649
            if mid - 1 >= 0:
                v_left = nums[mid-1]
            else:
                v_left = -2147483649            
            
            if v > v_right and v > v_left:
                answer= mid
                break
            elif v > v_right:
                r= mid - 1
                mid = r - ((r-l)//2)
            elif v > v_left:
                l = mid + 1
                mid = l + ((r-l)//2)
            else:
                l = mid
                mid = l + ((r-l)//2)
        return answer 
    