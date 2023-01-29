class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.len_ = 0
class Linkedlist():
    def __init__(self,data):
        self.head = Node(data)
        
    def append(self, data):
        pointer = self.head
        while pointer.next is not None:
            pointer  = pointer.next

        pointer.next = Node(data)
        
    def circle(self):
        pointer = self.head
        self.len_ = 1
        while pointer.next is not None:
            pointer  = pointer.next
            self.len_ += 1
        pointer.next = self.head
            
        
    def del_(self,index):
        index -=1
        pointer = self.head
        pre_index = index-1
        while pre_index>0:
            pointer = pointer.next
            pre_index -= 1
        del_value = pointer.next.data
        new_node = pointer.next.next
        pointer.next = new_node
        self.head = new_node
        self.len_ -= 1
        return del_value, self.len_



n, k = map(int, input().split())

a = Linkedlist(1)
for i in range(2,n+1):
    a.append(i) 
a.circle()

answers = []
result = a.del_(k)
answers.append(result[0])
while result[1]>0:
    result = a.del_(k)
    answers.append(result[0])


print("<" + ", ".join(list(map(str, answers))) + ">")



#################
N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]    # 맨 처음에 원에 앉아있는 사람들

answer = []   # 제거된 사람들을 넣을 배열
num = 0  # 제거될 사람의 인덱스 번호

for t in range(N):
    num += K-1
    if num >= len(arr):   # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈
        num = num % len(arr)

    answer.append(str(arr.pop(num)))
print("<", ", ".join(answer)[:], ">", sep='')
