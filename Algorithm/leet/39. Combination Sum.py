from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def back(start):
            summ = sum(comb)
            
            if summ == target:
                res.append(comb[:])
                return
            elif summ > target:
                return
            
            for idx in range(start,len(candidates)):
                comb.append(candidates[idx])
                back(idx)
                comb.pop()
        back(0)

        return res
