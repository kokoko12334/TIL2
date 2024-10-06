class StockSpanner:

    def __init__(self):
        self.arr = []
        self.cnt_arr = []

    def next(self, price: int) -> int:
        self.arr.append(price)
        cnt = 1
        n = len(self.arr)
        idx = n-2
        while idx >= 0 and self.arr[idx] <= price:
            cnt += self.cnt_arr[idx]
            idx -= self.cnt_arr[idx]

        self.cnt_arr.append(cnt)
        return cnt

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)