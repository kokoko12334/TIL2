import sys

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)  # 세그먼트 트리를 저장할 리스트
        self.build(data, 0, 0, self.n - 1)

    def build(self, data, node, start, end):
        if start == end:
            # leaf 노드인 경우
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            # 왼쪽 자식 노드와 오른쪽 자식 노드 구성
            self.build(data, 2 * node + 1, start, mid)
            self.build(data, 2 * node + 2, mid + 1, end)
            # 부모 노드의 값을 자식 노드 값으로 갱신
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, idx, value, node, start, end):
        if start == end:
            # 리프 노드에서 값 수정
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                # 왼쪽 서브트리 업데이트
                self.update(idx, value, 2 * node + 1, start, mid)
            else:
                # 오른쪽 서브트리 업데이트
                self.update(idx, value, 2 * node + 2, mid + 1, end)
            # 부모 노드의 값을 자식 노드 값으로 갱신
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, L, R, node, start, end):
        if R < start or end < L:
            # 구간이 겹치지 않음
            return 0
        if L <= start and end <= R:
            # 구간이 완전히 포함됨
            return self.tree[node]
        # 겹치는 구간에서 왼쪽과 오른쪽 서브트리로 나누어 쿼리 수행
        mid = (start + end) // 2
        left_sum = self.query(L, R, 2 * node + 1, start, mid)
        right_sum = self.query(L, R, 2 * node + 2, mid + 1, end)
        return left_sum + right_sum

input = sys.stdin.readline

n, m, k = [int(i) for i in input().split()]

arr = []
for _ in range(n):
    arr.append(int(input()))

seg_tree = SegmentTree(arr)

for _ in range(m+k):
    a, b, c = [int(i) for i in input().split()]

    if a == 1:
        seg_tree.update(b-1, c, 0, 0, n-1)
    else:
        result = seg_tree.query(b-1, c-1, 0, 0, n-1)
        print(result)

