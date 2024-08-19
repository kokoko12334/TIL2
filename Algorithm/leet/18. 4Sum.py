from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        arr = []
        nums = sorted(nums)
        n = len(nums)
        def dfs(idx):
            nonlocal n
            # print(idx, arr)
            if len(arr) > 4:
                return
            summ = sum(arr)
            # if summ > target:
            #     return
            if len(arr) == 4 and summ == target:
                arr2 = sorted([str(i) for i in arr])
                string = "".join(arr2)
                if string in seen:
                    return

                answer.append(arr[:]) 
                seen.add(string)

            for i in range(idx+1, n):
                arr.append(nums[i])
                dfs(i)
                arr.pop()

        answer = []
        seen = set()
        # print(nums)
        for i in range(n):
            arr.append(nums[i])
            dfs(i)
            arr.pop()
        
        return answer