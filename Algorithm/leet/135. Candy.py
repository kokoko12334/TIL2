from collections import defaultdict
from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        
        nums = set()
        n = len(ratings)
        dic = defaultdict(list)
        for i in range(n):
            nums.add(ratings[i])
            dic[ratings[i]].append(i)
        
        nums = sorted(nums)

        answer = [1]*n

        for num in nums:
            for idx in dic[num]:
                if idx - 1 >= 0:
                    if ratings[idx] > ratings[idx-1]:
                        answer[idx] = max(answer[idx], answer[idx-1] + 1)
                if idx + 1 < n:
                    if ratings[idx] > ratings[idx+1]:
                        answer[idx] = max(answer[idx], answer[idx+1] + 1)
        
        # print(dic)
        # print(nums)
        # print(ratings)
        # print(answer)
        return sum(answer)
