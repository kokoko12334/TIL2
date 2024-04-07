from bisect import bisect_left
from collections import defaultdict
from typing import List

#이분탐색
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        lis = []
        lis.append(nums[0])
        
        n = len(nums)
        idx_info = defaultdict(int)
        idx_info[nums[0]] = 0
        nn = 1
        for i in range(1,n):
            num = nums[i]
            # print(f"lis:{lis}, 맨끝:{lis[-1]}, 추가되는 숫자:{num}")
            if lis[-1] < num:
                lis.append(num)
                nn += 1
                idx_info[num] = nn-1
            else:
                idx = bisect_left(lis,num)
                lis[idx] = num
                idx_info[num] = idx
        

        # 원소 찾기 => idx_info로 삽입된 숫자들의 인덱스를 기록하고 역순으로 역추적하면서 찾기
        result = []
        idx = n-1
        for i in range(nn-1,-1,-1):
            for j in range(idx,-1,-1):
                if idx_info[nums[j]] == i:
                    result.append(nums[j])
                    idx -= 1
                    break
        
        return nn

#dp
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [1]*n
    
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        

        return max(dp)
