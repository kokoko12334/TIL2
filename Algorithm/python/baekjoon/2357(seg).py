import sys
import math

class SegmentTree:
    def __init__(self, arr):
        self.N = len(arr) - 1  # arr는 1-indexed
        self.arr = arr
        height = math.ceil(math.log2(self.N))
        tree_size = 1 << (height + 1)
        self.tree = [None] * tree_size
        self.build(1, 1, self.N)
    
    def build(self, node, start, end):
        if start == end:
            self.tree[node] = (self.arr[start], self.arr[start])
        else:
            mid = (start + end) // 2
            left = self.build(node * 2, start, mid)
            right = self.build(node * 2 + 1, mid + 1, end)
            self.tree[node] = (min(left[0], right[0]), max(left[1], right[1]))
        return self.tree[node]
    
    def query(self, node, start, end, l, r):
        # 구간이 겹치지 않으면 초기값 반환
        if r < start or end < l:
            return (1000000001, 0)
        # 구간이 완전히 포함되면 해당 노드 반환
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left_result = self.query(node * 2, start, mid, l, r)
        right_result = self.query(node * 2 + 1, mid + 1, end, l, r)
        return (min(left_result[0], right_result[0]), max(left_result[1], right_result[1]))

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] * (N + 1)
for i in range(1, N + 1):
    arr[i] = int(input().strip())
    
seg_tree = SegmentTree(arr)
    
output = []
for _ in range(M):
    a, b = map(int, input().split())
    res = seg_tree.query(1, 1, seg_tree.N, a, b)
    print(res[0], res[1])