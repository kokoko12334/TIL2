from collections import deque
import pickle
import time

class maxheap():
    def __init__(self, data):
        self.array = [None]
        self.array.append(data)

    def add_(self, data):
        self.array.append(data)
        child_idx = len(self.array)-1
        parent_idx = child_idx//2
        while self.array[parent_idx] < self.array[child_idx]:   #자식노드와 부모노드 비교하는 과정
            self.array[parent_idx], self.array[child_idx] = self.array[child_idx], self.array[parent_idx]
            child_idx = parent_idx
            parent_idx = child_idx//2
            if parent_idx == 0:   #루트노드에 도달하게 된다면 중단
                break

    def pop_(self):
        if len(self.array)>1:
            #루트노드 빼고 가장 마지막 노드를 루트노드에 대입
            left_pop_data = self.array[1]
            self.array[1] = self.array[-1]   
            self.array.pop()
            
            length = len(self.array)-1

            parent_idx = 1
            child_left = parent_idx*2
            child_right = child_left+1

            while child_left <= length or child_right <= length:
                stand = self.array[parent_idx]
                direction = ""
                if stand < self.array[child_left]:
                    stand = self.array[child_left]
                    direction = "L"
                #3개 남았을때 오른쪽부터 나가짐 그래서 오른쪽에 이 항목 추가(추가안하면 index에러남)    
                if child_right <= length and stand < self.array[child_right]:  
                    stand = self.array[child_right]
                    direction = "R"

                if direction == "L":
                    self.array[parent_idx], self.array[child_left] = self.array[child_left], self.array[parent_idx]     
                    parent_idx = child_left
                    child_left = parent_idx*2
                    child_right = child_left+1
                elif direction == "R":
                    self.array[parent_idx], self.array[child_right] = self.array[child_right], self.array[parent_idx]
                    parent_idx = child_right
                    child_left = parent_idx*2
                    child_right = child_left+1
                else:
                    break
            return left_pop_data       
        else:
            print("비었습니다.")                

heap = maxheap(20)

heap.add_(10)
heap.add_(15)
heap.add_(1)
heap.add_(6)
heap.add_(8)
heap.add_(29)
heap.array

##데이터 삽입
heap.add_(21)
heap.array

#데이터 삭제
heap.pop_()
heap.array

start = time.time()
with open("./list_data.pickle", "rb") as f:
    lst = pickle.load(f)


heap = maxheap(lst[0])
for i in lst[1:]:
    heap.add_(i)


sorted_lst = []
for _ in range(len(heap.array)-1):
    b = heap.pop_()
    sorted_lst.append(b)

end = time.time()
print("걸린 시간: {}".format(end-start))



