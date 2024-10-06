import sys
from collections import deque

num = int(sys.stdin.readline())

que = deque(range(1,num+1))

while True:
    if len(que) == 1:
        break
    que.popleft()  #버리고
    que.append(que.popleft())  #앞에 있는 것을 뒤에 붙히고
   
print(que[0])
