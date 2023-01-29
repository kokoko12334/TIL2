from Heap_array import maxheap
from queue import PriorityQueue
from collections import deque
from heapq import *
import pickle
import time
#######직접 구현한거#############

with open("./list_data.pickle", "rb") as f:
    lst = pickle.load(f)

start = time.time()
heap = maxheap(lst[0])
for i in lst[1:]:
    heap.add_(i)


sorted_lst = []
for _ in range(len(heap.array)-1):
    b = heap.pop_()
    sorted_lst.append(b)

end = time.time()
print("힙정렬의 걸린 시간: {}".format(end-start))

print(sorted_lst)


#####내장모듈#######(둘 다 최소힙임.)

# piorityqueue는 Thread safe 를 확인 그래서 heapq가 더 빠름
que = PriorityQueue()
lst = [29,20,10,15,1,6,8,21]

for i in lst:
    que.put(i)

que.get()


####heap
lst = [29,20,10,15,1,6,8,21]

heap_ = []   #힙구조를 담을 리스트를 따로 만든다.

for i in lst:
    heappush(heap_, i)
print(heap_)

#pop
heappop(heap_)
print(heap_)


# 최소힙이므로 1234 에서 우선순위가 높은 값은 1이다.
# 이때 -1 -2 -3 -4 를 해준다면 즉, 부호를 바꾸면 이때 우선순위가 높은값은 -4가 된다.

lst = [29,20,10,15,1,6,8,21]
heap_ = []
for i in lst:
    heappush(heap_,(-i,i))
print(heap_)

###heapify
lst = [29,20,10,15,1,6,8,21]
heapify(lst)
print(lst)


###nsamllest
lst = [29,20,10,15,1,6,8,21]
nsmallest(3, lst)

##nlargest
lst = [29,20,10,15,1,6,8,21]
nlargest(3, lst)


