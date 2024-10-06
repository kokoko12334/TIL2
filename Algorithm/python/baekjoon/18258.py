import sys

from collections import deque

que = deque()
    
num = int(sys.stdin.readline())


for _ in range(num):
    a = sys.stdin.readline().split()

    if a[0] == 'push':
        que.append(a[1])

    elif a[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)

    elif a[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)

    elif a[0] == 'back':
        if que:
            print(que[-1])   
        else:
            print(-1)                             
    
    elif a[0] == 'size':
        if que:
            print(len(que))
        else:
            print(0)

    elif a[0] == 'pop':
        if que:
            r = que.popleft()
            print(r)
        else:
            print(-1)                
