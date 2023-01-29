from collections import deque


class Node():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.parent = None      #부모 노드를 참조해야 하기 때문에 양방향으로 표현

class heap():
    def __init__(self, data):
        self.root = Node(data)
        
    
    def heap_max(self, data):
        pointer = self.root
        #추가할 노드를 맨 밑 층에 넣는 과정
        while True:       
            
            if pointer.left == None:  #왼쪽부터 탐색
                pointer.left = Node(data)
                pointer.left.parent = pointer  #양 방향 연결
                pointer = pointer.left  # 다음 과정을 위해 추가한 노드로 이동

                break
            else:
                if pointer.right == None:   #그다음 오른쪽
                    pointer.right = Node(data)
                    pointer.right.parent = pointer 
                    pointer = pointer.right
                    break    
                elif pointer.left.left == None or pointer.left.right == None:  #왼쪽 노드의 자식이 하나라도 빈다면 왼쪽으로(완전이진트리 방식)
                    pointer = pointer.left    
                                                        
                elif pointer.right.left == None or pointer.right.right == None:
                    pointer = pointer.right  
                else: #왼쪽, 오른쪽 노드의 자식 노드가 다 찼다면 그때는 왼쪽으로 이동
                    pointer = pointer.left

        #자식 노드가 부모노드 보다 크면 이동
        while pointer.data >= pointer.parent.data:
            pointer.data, pointer.parent.data = pointer.parent.data, pointer.data
            pointer = pointer.parent
            if pointer.parent == None:
                break

    
    def levelorder(self):
        que = deque()
        lst = []

        pointer = self.root  # 처음은 루트노드
        que.append(pointer)

        def reg(pointer):
            que.popleft()
            print(pointer.data) # que에 나오면서 출력
            lst.append(pointer) 

            if pointer.left != None:  # 자식노드 큐에 삽입
              que.append(pointer.left)
            if pointer.right != None:
              que.append(pointer.right)
            if que:
              reg(que[0])
            return lst
           
        lst = reg(pointer)
        return lst
    
    def heap_pop(self):
        pointer = self.root
        lst = self.levelorder()
        bottom_node = lst[-1]
        
        pointer.data = bottom_node.data  #노드의 값을 루트 노드에 삽입

        parent_node = bottom_node.parent  #가장 아래의 노드를 끊는 과정
        if parent_node.left.data == bottom_node.data:
            parent_node.left = None
        elif parent_node.right.data == bottom_node.data:
            parent_node.right = None    


        while (pointer.data < pointer.left.data and pointer.left.data !=None) or (pointer.data < pointer.right.data and pointer.right.data != None):
            if pointer.right.data == None:
                if pointer.data < pointer.left.data:
                    pointer.data, pointer.left.data = pointer.left.data, pointer.data
                    pointer = pointer.left
            elif pointer.left.data == None:
                if pointer.data < pointer.right.data:
                    pointer.data, pointer.right.data = pointer.right.data, pointer.data
                    pointer = pointer.right


            if pointer.left.data != None and pointer.right.data != None:

                if pointer.data < pointer.left.data and pointer.left.data > pointer.right.data :
                    pointer.data, pointer.left.data = pointer.left.data, pointer.data
                    pointer = pointer.left    
                elif pointer.data < pointer.right.data and pointer.right.data > pointer.left.data:
                    pointer.data, pointer.right.data = pointer.right.data, pointer.data
                    pointer = pointer.right
            if pointer.left == None and pointer.right == None:
                break





a = heap(29)
a.heap_max(20)
a.heap_max(10)
a.heap_max(15)
a.heap_max(1)
a.heap_max(6)
a.heap_max(8)

a.heap_max(21)

a.levelorder()

a.heap_pop()


