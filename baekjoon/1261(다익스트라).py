from collections import deque
import sys
input = sys.stdin.readline
n,m = [int(i) for i in input().split()]
# n가로 m세로


lst = [input() for _ in range(m)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
q = deque()
q.append([0,0])
visited = [[-1]*n for _ in range(m)]
visited[0][0] = 0
while q:
    y,x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if nx < 0 or nx>=n or ny < 0 or ny >= m:
            continue
        
        if visited[ny][nx] == -1:
            if lst[ny][nx] == "0":
                q.appendleft([ny,nx]) #0이면 우선적으로 탐색
                visited[ny][nx] = visited[y][x]
            else:
                q.append([ny,nx])
                visited[ny][nx] = visited[y][x] + 1


print(visited[m-1][n-1])