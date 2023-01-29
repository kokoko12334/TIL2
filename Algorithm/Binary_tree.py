from collections import deque
#기본개념
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

a = Node(1)
a.right = Node(2)
a.left = Node(3)



class Bst:
    def __init__(self, data):
        self.root = Node(data)

    def add_(self,data):
        pointer = self.root
        while True:
            if data > pointer.data:      
                if pointer.right == None:     #그 자리가 None이면 바로 대입
                    pointer.right = Node(data)
                    break
                else:                    #아니면 그 자리로 이동
                    pointer = pointer.right 
            elif data < pointer.data:
                if pointer.left == None:
                    pointer.left = Node(data)
                    break
                else:
                    pointer = pointer.left 
    def search(self, data):
        pointer = self.root
        process = []
        while True:
            if data > pointer.data:
                
                if pointer.right == None:
                    print('데이터가 없습니다.')
                    process = []       
                    break
                else:
                    process.append('R')
                    if pointer.right.data == data:
                        break
                    else:
                        pointer = pointer.right
            elif data < pointer.data:
                
                if pointer.left == None:
                    print('데이터가 없습니다.')
                    process = []       
                    break                
                else:
                    process.append('L')
                    if pointer.left.data == data:
                        break
                    else:
                        pointer = pointer.left
            else:
                return [0]
        return process                       

    def preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.preorder(node.left)  #재귀끝나면 그 아래꺼 실행
            self.preorder(node.right)
    def inorder(self, node):
        if node:
            
            self.inorder(node.left)  #재귀끝나면 그 아래꺼 실행
            print(node.data, end=' ')
            self.inorder(node.right)
    def posterorder(self, node):
           if node:

               self.posterorder(node.left)  #재귀끝나면 그 아래꺼 실행
               self.posterorder(node.right)
               print(node.data, end=' ')
    def levelorder(self):
        que = deque()
        
        pointer = self.root #처음은 루트노드
        que.append(pointer)
        
        def reg(pointer):
            que.popleft()    
            print(pointer.data) #que에 나오면서 출력

            if pointer.left != None: #자식노드 큐에 삽입
              que.append(pointer.left)
            if pointer.right != None:  
              que.append(pointer.right)
            if que:   
              reg(que[0])

        reg(pointer)    


a = Bst(10)
a.add_(7)
a.add_(6)
a.add_(8)
a.add_(15)
a.add_(13)
a.add_(17)
a.add_(30)
a.add_(31)


a.preorder(a.root)
a.inorder(a.root)
a.posterorder(a.root)

a.levelorder()

