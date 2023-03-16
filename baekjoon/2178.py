from collections import deque
import sys
sys.setrecursionlimit(10**6)

n, m = [int(i) for i in input().split()]
lst = []
for _ in range(n):
  a = [int(i) for i in input()]
  lst.append(a)


###x가 위아래 y가 좌우
dy = [0,1,0,-1]
dx = [-1,0,1,0]

seen = {}
que = deque()
x = 0
y = 0
s = str(x)+"."+str(y)
que.append(s)
seen[s] = True
def bfs():
    if que:
        s = que.popleft().split(".")
        x = int(s[0])
        y = int(s[1])
        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]
            if new_x <0 or new_y >= m or new_x >= n or new_y < 0:
              continue
            if lst[new_x][new_y] == 1 and str(new_x)+str(new_y) not in seen:
              lst[new_x][new_y] = lst[x][y]+1
              s2 = str(new_x)+"."+ str(new_y)
              que.append(s2)
              seen[s2] = True
        bfs()        



bfs()

print(lst[n-1][m-1])



