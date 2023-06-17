from collections import deque
import sys
input = sys.stdin.readline
n = int(input())

q= deque([[0,n]])
seen = {i:0 for i in range(1,n+1)}

while q:
    parent, num = q.popleft()
    
    if num == 1:
        break
    if not num%3:
        next = num//3
        if not seen[next]:
            seen[next] = num
            q.append([num, next])
    if not num%2:
        next = num//2
        if not seen[next]:
            seen[next] = num
            q.append([num,next])
    next = num - 1
    if next>=1 and not seen[next]:
        seen[next] = num
        q.append([num,next])

answer = [1]
check = 1
cnt = -1
while check:
    answer.append(seen[check])
    check = seen[check]
    cnt += 1
print(cnt)
print(*answer[::-1][1:])