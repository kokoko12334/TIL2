from heapq import *
class SmallestInfiniteSet:

    def __init__(self):
        self.arr = [i for i in range(1,1001)]
        self.sett = {i for i in range(1,1001)}
        heapify(self.arr)        

    def popSmallest(self) -> int:
        num = heappop(self.arr)
        self.sett.remove(num)
        return num

    def addBack(self, num: int) -> None:
        if num not in self.sett:
            heappush(self.arr,num)
            self.sett.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)