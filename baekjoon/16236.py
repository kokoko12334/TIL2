from heapq import *
from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
lst = [[int(i) for i in input().split()] for _ in range(n)]

seen = [[0]*n for _ in range(n)]
q = deque()
flag = True
for i in range(n):
    if flag:
        for j in range(n):
            if lst[i][j] == 9:
                q.append([i,j,0])
                seen[i][j] = 1
                lst[i][j] = 0
                flag = False
                break
size = 2            
dx = [0,-1,0,1]
dy = [-1,0,1,0]
eat = []
answer = 0
fish = 0
while q:
    y,x,d = q.popleft()
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if nx <0 or nx>=n or ny < 0 or ny >= n:
            continue
        if not seen[ny][nx]:
            if lst[ny][nx] and lst[ny][nx] < size:
                q.append([ny,nx,d+1]) 
                seen[ny][nx] = 1
                eat.append([ny,nx,d+1])
                
            elif not lst[ny][nx] or lst[ny][nx] == size:
                q.append([ny, nx, d+1])
                seen[ny][nx] = 1
    if q and q[0][2] == d+1 and eat:
        eat.sort()
        y2,x2,d2 = eat[0]
        q = deque([[y2,x2,0]])
        lst[y2][x2] = 0
        answer += d2
        eat = []
        seen = [[0]*n for _ in range(n)]
        seen[y2][x2] = 1
        fish += 1
        if size == fish:
            size += 1
            fish = 0


print(answer)



