
#오른쪽이동 -> (i+1)%len
# 왼쪽이동 -> (i-1)%len
import sys
from collections import deque

def right(que):
    a = que.pop()
    return que.appendleft(a)
def left(que):
    a = que.popleft()
    return que.append(a)    

n, m = [int(i) for i in sys.stdin.readline().split()]

lst = [int(i) for i in sys.stdin.readline().split()]

que = deque(range(1,n+1))

cnt = 0
for i in lst:
    k = que.index(i)
    left_move = k
    right_move = len(que)-k
    if left_move >= right_move:
        cnt += right_move
        for _ in range(right_move):
            right(que)
    else:
        cnt += left_move
        for _ in range(left_move):
            left(que)
    que.popleft()
    
print(cnt)

