from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        arr = sorted(points, key=lambda x:x[1])

        e = arr[0][1]
        n = len(arr)
        answer = 1
        for i in range(1,n):
            s = arr[i][0]

            if s > e:
                answer += 1
                e = arr[i][1]

        return answer