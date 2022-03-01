##스택 나중에 들어온 것이 먼저 삭제
lst = []
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.pop()
lst.append(5)
print(lst)


#큐 먼저 들어온 것이 먼제 삭제
from collections import deque

queue = deque()

queue.append(5)
queue.append(4)
queue.append(3)
queue.append(2)
queue.append(1)
queue.popleft()
queue.append(6)
print(queue)


#우선순위 큐

import sys
import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)

    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = input()

arr = []

for i in range(n):
    arr.append(int(input()))



res = heapsort(arr)


for i in range(n):
    print(res[i])


n = int(input())





















