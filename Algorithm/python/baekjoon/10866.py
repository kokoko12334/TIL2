import sys
from collections import deque

num = int(sys.stdin.readline())

deck = deque()
for _ in range(num):

    k = sys.stdin.readline().split()
    
    if k[0] == 'empty':
        if deck:
            print(0)
        else:
            print(1)    

    elif k[0] == 'push_front':
        deck.appendleft(k[1])        
    
    elif k[0] == 'push_back':
        deck.append(k[1])
    
    elif k[0] == 'pop_front':
        if deck:
            r = deck.popleft()
            print(r)
        else:
            print(-1)
    
    elif k[0] == 'pop_back':
        if deck:
            r = deck.pop()
            print(r)
        else:
            print(-1)
    
    elif k[0] == 'size':
        print(len(deck))

    elif k[0] == 'front':
        if deck:
            print(deck[0])
        else:
            print(-1)

    elif k[0] == 'back':
        if deck:
            print(deck[-1])
        else:
            print(-1)


