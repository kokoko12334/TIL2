import math
from collections import deque
from bisect import bisect_left

max_int32 = 2147483647
class Node:

    def __init__(self, degree):
        self.values = deque([max_int32] * (degree - 1))
        self.parent = None
        self.child = [None] * (degree+1)
        self.leaf = True

class BTree:

    def __init__(self, degree):
        self.degree = degree
        self.root = Node(degree)
        self.max_key = degree - 1
        self.min_key = math.ceil(degree/2) - 1
    
    def insert(self, key):

        node = self.root
        #리프노드까지 내려가기
        while not node.leaf:
            
            i = bisect_left(node.values, key)
            if node.values[i] == max_int32 or node.values[i] > key:
                node = node.child[i]
            else:
                node = node.child[i + 1]

        # 키 삽입
        i = bisect_left(node.values, key)
        node.values.insert(i, key)
        node.values.pop()  # max_int32 제거

        # 노드 분할
        if len(node.values) > self.max_key:
            self.split(node)
        
    def split(self, node):
        mid_index = self.max_key // 2
        mid_value = node.values[mid_index]

        # 새로운 노드 생성
        new_node = Node(self.degree)
        new_node.values = deque([max_int32] * (self.degree - 1))
        new_node.leaf = node.leaf
        new_node.values.extend(node.values[mid_index + 1:])
        new_node.child = node.child[mid_index + 1:]
        node.values = deque(list(node.values[:mid_index]) + [max_int32] * (self.degree - 1 - mid_index))
        node.child = node.child[:mid_index + 1]

        if node.parent:
            parent = node.parent
        else:
            # 새로운 루트 생성
            parent = Node(self.degree)
            parent.leaf = False
            parent.child[0] = node
            self.root = parent
            node.parent = parent
            new_node.parent = parent

        i = bisect_left(parent.values, mid_value)
        parent.values.insert(i, mid_value)
        parent.values.pop()  # max_int32 제거
        parent.child.insert(i + 1, new_node)

        if len(parent.values) > self.max_key:
            self.split(parent)

        #자기 자리 찾아가기 => leaf True일때까지
        #삽입 => node가 차면 다시 분기

# 사용 예
btree = BTree(3)
for key in [10, 20, 5, 6, 12, 30, 7, 17]:
    btree.insert(key)


print(btree.root.values)