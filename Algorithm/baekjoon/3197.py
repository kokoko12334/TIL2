
from collections import deque
import sys
input = sys.stdin.readline
row, col = [int(i) for i in input().split()]

lst = [list(input()) for _ in range(row)]


def find(parent, idx):
    y, x = idx[0], idx[1]
    if parent[y][x] != [y, x]:
        parent[y][x] = find(parent, parent[y][x])
    return parent[y][x]


def union(idx1, idx2, parent, rank):
    xroot = find(parent, idx1)
    yroot = find(parent, idx2)

    if xroot == yroot:
        return
    if rank[xroot[0]][xroot[1]] < rank[yroot[0]][yroot[1]]:
        parent[xroot[0]][xroot[1]] = yroot
    elif rank[xroot[0]][xroot[1]] > rank[yroot[0]][yroot[1]]:
        parent[yroot[0]][yroot[1]] = xroot
    else:
        parent[xroot[0]][xroot[1]] = yroot
        rank[yroot[0]][yroot[1]] += 1


parent = [[[i, j]for j in range(col)]for i in range(row)]
rank = [[0]*col for _ in range(row)]
swans = []
q = deque()
seen = [[0]*col for _ in range(row)]
for i in range(row):
    for j in range(col):
        if lst[i][j] == "L":
            swans.append([i, j])
            lst[i][j] = "."
            q.append([i,j])
            seen[i][j] = 1
        elif lst[i][j] == ".":
            q.append([i,j])
            seen[i][j] = 1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = 0
next = []
while q:
    out = q.popleft()
    y, x= out[0], out[1]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if nx < 0 or nx >= col or ny < 0 or ny >= row:
            continue
        if lst[ny][nx] == ".":
            if find(parent, [ny, nx]) != find(parent, [y, x]):
                union([ny, nx], [y, x], parent, rank)
                q.append([ny, nx])
        
        elif lst[ny][nx] == "X" and not seen[ny][nx]:
            union([ny, nx], [y, x], parent, rank)
            next.append([ny, nx])
            seen[ny][nx] = 1
            

answer = 0
while find(parent, swans[0]) != find(parent, swans[1]):
    
    answer += 1
    q = deque(next)
    next = []
    while q:
        out = q.popleft()
        
        y, x = out[0], out[1]
        lst[y][x] = "."
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx >= col or ny < 0 or ny >= row:
                continue
            if lst[ny][nx] == ".":
                if find(parent, [ny, nx]) != find(parent, [y, x]):
                    union([ny, nx], [y, x], parent, rank)
                    q.append([ny, nx])
            
            elif lst[ny][nx] == "X" and not seen[ny][nx]:
                seen[ny][nx] = 1
                union([ny, nx], [y, x], parent, rank)
                next.append([ny, nx])

print(answer)
