
from collections import deque
import sys
input = sys.stdin.readline
n,m = [int(i) for i in input().split()]

lst = [[int(i)for i in input().split()] for _ in range(n)]
lst2 = [[0]*m for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def search(q,cnt):
    seen = [[0]*m for _ in range(n)]
    stack = [q[0]]
    seen[q[0][0]][q[0][1]] = 1
    cnt2 = 0
    while stack:
        y,x,d = stack.pop()
        cnt2 += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx>=m or ny < 0 or ny >=n:
                continue
            if not seen[ny][nx] and lst[ny][nx]:
                stack.append([ny,nx,d])
                seen[ny][nx] = 1

    if cnt2 == cnt:
        return True
    else:
        return False


q = deque()
cnt = 0
for i in range(n):
    for j in range(m):
        if lst[i][j]:
            q.append([i,j,0])
            cnt += 1



while search(q,cnt):
    now = q[0][2]
    while q:
        if q[0][2] != now:
            lst = [lst2[k][:]for k in range(n)]
            break
        y,x,d = q.popleft()
        v = lst[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx>=m or ny < 0 or ny>=n:
                continue
            if not lst[ny][nx]:
                v -= 1
                if v < 0:
                    v = 0
                    break
        lst2[y][x] = v
        if v:
            q.append([y,x,d+1])
        else:
            cnt -= 1
    if not q:
        break

if cnt:
    print(now + 1)
else:
    print(cnt)






