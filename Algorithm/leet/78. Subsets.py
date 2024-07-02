from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def dfs(idx):
            if idx == n - 1:
                answer.append(res[:])
                return
            
            res.append(nums[idx+1])
            dfs(idx+1)
            res.pop()
            dfs(idx+1)

        answer = []
        res = []
        dfs(-1)
        return answer