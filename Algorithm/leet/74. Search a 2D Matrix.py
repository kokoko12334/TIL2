from bisect import bisect_right
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = len(matrix)
        col = len(matrix[0])

        f = []
        for i in range(row):
            f.append(matrix[i][0])

        row_idx = bisect_right(f,target) - 1
        arr = matrix[row_idx]
        l = 0
        r = len(arr) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] < target:
                l = mid + 1
            elif arr[mid] > target:
                r = mid - 1
            else:
                return True
        
        return False
