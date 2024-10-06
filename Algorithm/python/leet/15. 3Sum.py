from typing import List
class Solution:
    
    def twoPointer(self,seen,answer,arr,target):
        
        l = 0
        r = len(arr) - 1
        
        while l < r:
            s = arr[l] + arr[r]
            
            if s == target:
                lst = [-target,arr[l],arr[r]]
                lst.sort()
                check = str(lst)
                if check not in seen:
                    answer.append(lst)
                    seen.add(check)
                l += 1
            elif s < target:
                l += 1
            else:
                r -= 1

    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        hashMap = {}
        seen = set()
        nums.sort()
        
        for i in range(len(nums)):
            arr = nums[:i] + nums[i+1:]
            num = nums[i]
            if num not in hashMap: 
                self.twoPointer(seen,answer,arr,-num)
                hashMap[num] = i

        return answer




        