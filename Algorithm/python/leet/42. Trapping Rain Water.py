from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max_arr = [0]*n
        r_max_arr = [0]*n

        l_max = 0
        for i in range(n):
            l_max = max(l_max, height[i])
            l_max_arr[i] = l_max

        r_max = 0
        for i in range(n-1,-1,-1):
            r_max = max(r_max, height[i])
            r_max_arr[i] = r_max

        # 한칸에서 왼쪽에서 가장 큰 높이, 오른쪽에서 가장 큰 높이 에서 자기자신을 뺀거
        water = 0
        for i in range(n):
            water += min(l_max_arr[i], r_max_arr[i]) - height[i]

        return water        