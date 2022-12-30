
#기본적인 개념형태

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

# 각 노드들 생성
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

#노드 연결
n1.next = n2
n2.next = n3
n3.next = n4




