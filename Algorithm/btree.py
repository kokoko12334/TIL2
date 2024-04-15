import math
from collections import deque
from bisect import bisect_left

max_int32 = 2147483647
class Node:

    def __init__(self, degree):
        self.values = deque([max_int32]* (degree - 1))
        self.parent = None
        self.child = [None] * (degree+1)
        self.leaf = True

class BTree:

    def __init__(self, degree):
        self.degree = degree
        self.root = Node(degree)
        self.max_key = degree - 1
        self.min_key = math.ceil(degree/2) - 1
    
    def insert(self, num):

        node = self.root
        #리프노드까지 내려가기
        while node.leaf == False:
            idx = bisect_left(node.values, num)
            if idx:
                node = node.child[idx - 1]
            else:
                node = node.child[idx]
        
        #노드에 데이터 삽입
        idx = bisect_left(node.values, num)
        node.values.insert(idx, num)

        n = len(node.values)
        if n > self.max_key:
            median = node.values[n//2]
            parent_node = node.parent
            if parent_node == None:
                self.root = Node(self.degree)
                self.root.leaf = False
                parent_node = self.root
            
            idx = bisect_left(parent_node.values, num)
            parent_node.values.insert(idx, num)

            left_node = Node(self.degree)
            right_node = Node(self.degree)
            left_node.values = node.values[:median]
            right_node.values = node.values[median+1:]

            parent_node.child
        


        #자기 자리 찾아가기 => leaf True일때까지
        #삽입 => node가 차면 다시 분기

a = deque([3,5,7])
a[2]
a.insert(2,4)
a

bisect_left([1,2,3],5)
len(a)

a.insert()