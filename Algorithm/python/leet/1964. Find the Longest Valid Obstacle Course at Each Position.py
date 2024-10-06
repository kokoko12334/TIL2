from typing import List
from bisect import bisect_right
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        
        n = len(obstacles)
        lis = [obstacles[0]]
        answer = [0]*n
        answer[0] = 1
        cnt = 1
        for i in range(1, n):
            num = obstacles[i]
            if lis[-1] <= num:
                lis.append(num)
                cnt += 1
                answer[i] = cnt 
            else:
                idx = bisect_right(lis, num)
                lis[idx] = num
                answer[i] = idx + 1

        return answer
