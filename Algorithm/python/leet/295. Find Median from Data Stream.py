from bisect import bisect_right
import heapq
class MedianFinder:

    def __init__(self):
        self.arr = []
        self.n = 0

    def addNum(self, num: int) -> None:
        idx = bisect_right(self.arr, num)
        self.arr.insert(idx, num)
        self.n += 1
        
        # print(self.arr, idx)
    def findMedian(self) -> float:
        # return 0.0
        if self.n%2:
            mid = self.n // 2
            return self.arr[mid]
        else:
            mid1 = self.n//2
            mid2 = mid1 - 1
            
            return (self.arr[mid1] + self.arr[mid2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()



class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # Initialize two heaps: small to store the smaller half as a max heap
        # and large to store the larger half as a min heap
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # If large heap is not empty and the number is greater than the smallest number in large heap,
        # push it to the large heap. Otherwise, push the negation of the number to the small heap.
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        # Balance the heaps by adjusting their sizes if necessary
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # If sizes of both heaps are equal, return the average of the maximum element in the small heap
        # and the minimum element in the large heap
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0