from heapq import *
import sys


#n: 보석의 개수 k: 가방의 개수
# m:무게 v:가치
#c: 가방의 무게제한

n,k = [int(i) for i in sys.stdin.readline().split()]


lst = []
for _ in range(n):
    m,v = [int(i) for i in sys.stdin.readline().split()]
    lst.append([m,v])
    
lst.sort(key=lambda x: x[0])

bag = []
for _ in range(k):
    bag.append(int(input()))
bag.sort()


answer = 0
heap_q = []
idx = 0
for i in bag:
    
    while idx<= n-1 and lst[idx][0] <= i:
        m,v = lst[idx][0], lst[idx][1]
        heappush(heap_q, -v)
        idx += 1
    if heap_q:
        answer += (-1)*heappop(heap_q)


print(answer)
