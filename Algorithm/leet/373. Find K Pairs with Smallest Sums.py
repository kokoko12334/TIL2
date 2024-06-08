import heapq
from typing import List
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k <= 0:
            return []

        # 첫 번째 요소와 nums2의 각 요소로 구성된 쌍을 힙에 초기화
        min_heap = []
        for j in range(min(k, len(nums2))):  # nums2의 처음 k개 쌍만 필요
            heapq.heappush(min_heap, (nums1[0] + nums2[j], 0, j))

        result = []
        while min_heap and len(result) < k:
            sum, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1):  # i가 배열을 벗어나지 않으면 다음 쌍 (i+1, j) 추가
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))
        
        return result