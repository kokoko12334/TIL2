import sys
input = sys.stdin.readline
n, m = [int(i) for i in input().split()]

matrix = []
for _ in range(n):
    arr = [int(i) for i in input().split()]
    matrix.append(arr)

path = []
for _ in range(m):
    i,j = [int(k) - 1 for k in input().split()]
    path.append((i,j))

dy = [0,1,0,-1]
dx = [1,0,-1,0]

seen = [[0]*n for _ in range(n)]
answer = 0
path_set = set(path)
def dfs(y, x, idx):
    # print(y,x, idx)
    global answer
    
    if (y,x) in path_set:
        if path[idx] != (y, x):
            return
        else:
            idx += 1
            
            if idx == m:
                answer += 1
                return

    for i in range(4):
        
        ny = y + dy[i]
        nx = x + dx[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
    
        if matrix[ny][nx] == 0 and not seen[ny][nx]:
            seen[ny][nx] = 1
            dfs(ny,nx, idx)
            seen[ny][nx] = 0
            
    
init = (path[0][0], path[0][1])

seen[init[0]][init[1]] = 1

dfs(init[0],init[1], 0)

print(answer)









    