from collections import deque
import sys
a, b = [int(i) for i in sys.stdin.readline().split()]

que = deque([[a,0]])
seen = {a}

answer = 0
flag = False
while que:

    out = que.popleft()
    num = out[0]
    level = out[1]    
    for i in [num*2, (num*10)+1]:
        if i not in seen and i < b:
            que.append([i,level+1])
            seen.add(i)
        elif i == b:
            answer = level + 1
            flag = True
            break
    if flag:
        break

if answer:
    print(answer + 1)
else:
    print(-1)    