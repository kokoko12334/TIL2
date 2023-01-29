
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



class Linkdlist:
    def __init__(self,data):
        self.head = Node(data) #head가 노드의 객체가 된다.

    def append(self, data):
        pointer = self.head  #head부터 출발
        while pointer.next is not None:
            pointer = pointer.next   #None이 아니면 그다음 노드로 진행
        pointer.next = Node(data)  #끝에 도달하고 거기에 append

    def print_(self):
        pointer = self.head
        while pointer.next is not None:
            print(pointer.data)
            pointer = pointer.next
        print(pointer.data)    #앞에서 마지막것은 while문에 들어가지 못하므로 여기에서 마지막것도 출력
    
    def get_data(self, index):
        pointer = self.head
        while index> 0:
            pointer = pointer.next
            index -=1
        return pointer.data

    def add_(self,index, data):
        add_node = Node(data)
        pre_index = index-1
        pointer = self.head
        while pre_index>0:
            pointer = pointer.next
            index -=1
        after_node = pointer.next  #끊기전에 원래 노드    
        pointer.next = add_node   #노드 새로연결
        add_node.next = after_node  #새로운노드의 next지정

    def delete_(self, index):
        pointer = self.head
        pre_index = index-1   #삭제할 인덱스 직전
        while pre_index>0:
            pointer = pointer.next
            index -= 1
        after_node = pointer.next.next #해당 인덱스에서 두칸(중간이 삭제할 인덱스이므로) 이동
        pointer.next = after_node  #next를 해당 노드에 연결

#######노드들 연결        
a = Linkdlist(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.append(6)
a.print_()


######두번째 노드값
a.get_data(1)

#두번째 자리에 새로운 노드 삽입
a.add_(1,'k')
a.print_()

#두번째 노드 삭제
a.delete_(1)
a.print_()





