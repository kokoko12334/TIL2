import sys
from collections import deque

def bfs(v):
    
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return array[v]
        for next_v in (v-1, v+1, 2*v):
            if 0 <= next_v < max and not array[next_v]:
                array[next_v] = array[v] + 1
                q.append(next_v)


max = 100001
n, k = [int(i) for i in sys.stdin.readline().split()]
array = [0] * max
print(bfs(n))






