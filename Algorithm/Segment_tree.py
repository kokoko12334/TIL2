class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        # Initialize the leaves of the segment tree
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # Build the segment tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
    
    def update(self, index, value):
        # Update the value at index
        pos = self.n + index
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]
    
    def query(self, left, right):
        # Query the sum from left to right (inclusive)
        result = 0
        left += self.n
        right += self.n + 1
        while left < right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result

# 사용 예시
data = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(data)

print(seg_tree.query(1, 3))  # 3 + 5 + 7 = 15
seg_tree.update(1, 10)
print(seg_tree.query(1, 3))  # 10 + 5 + 7 = 22

seg_tree.update(2, 123)
print(seg_tree.query(1, 3))  # 10 + 5 + 7 = 22