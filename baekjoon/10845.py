import sys
from collections import deque



n = int(sys.stdin.readline())

commands = []
for _ in range(n):
    commands.append(sys.stdin.readline().split())


que = deque()
for i in commands:

    if i[0] == "push":
        que.append(i[1])
    elif i[0] == "pop":
        if que:
            print(que.popleft())
        else:
            print(-1)        
    elif i[0] == "size":
        print(len(que))
    elif i[0] == "empty":
        if que:
            print(0)
        else:
            print(1)
    elif i[0] == "front":
        if que:
            print(que[0])            
        else:
            print(-1)
    elif i[0] == "back":
        if que:
            print(que[-1])
        else:
            print(-1)    
