import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m  = [[0]*n for _ in range(n)]

k = int(input())
for _ in range(k):
    y, x = [int(i)-1  for i in input().split()]
    m[y][x] = 1

l = int(input())
move = {}
for _ in range(l):
    s, d = input().split()

    move[int(s)] = d


change_d = {
    'rL':[(-1, 0), 'u'],
    'rD':[(1, 0),'d'],
    'dL':[(0, 1), 'r'],
    'dD':[(0, -1), 'l'],
    'lL':[(1, 0), 'd'],
    'lD':[(-1, 0), 'u'],
    'uL':[(0, -1), 'l'],
    'uD':[(0, 1), 'r']
}

q = deque([(0,0,'r')])
go = [0,1]
body = deque([(0,0)])
m[0][0] = -1
s = 0
answer = 0

while q:
    y, x, d = q.popleft()
    s += 1
    ny = y + go[0]
    nx = x + go[1]

    if nx < 0 or nx >= n or ny < 0 or ny >= n or m[ny][nx] == -1:
        answer = s
        break
    
    if m[ny][nx] != 1:
        t_y, t_x = body.popleft()
        m[t_y][t_x] = 0
    else:
        m[ny][nx] = 0
    m[ny][nx] = -1
    if s in move.keys():
        keyy = d + move[s]
        go, d = change_d[keyy]
    
    body.append([ny, nx])
    q.append((ny, nx, d))


print(answer)