from collections import deque
from itertools import combinations_with_replacement
n,m = [int(i) for i in input().split()]



# bfs
for j in range(1,n+1):
    q = deque([[[j],1]])
    while q:
        idx,level = q.popleft()
        if level == m:
            print(*idx)
            continue
        start = idx[-1]
        for i in range(start,n+1):

            q.append([idx+[i],level+1])


#itertools
lst = list(combinations_with_replacement(range(1,n+1),m))

for i in lst:
    print(*i)


