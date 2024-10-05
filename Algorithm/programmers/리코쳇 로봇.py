from collections import deque
def solution(board):
    answer = 0
    r = len(board)
    c = len(board[0])
    q = deque()
    matrix = [[-1]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] == "R":
                matrix[i][j] = 0
                q.append((i,j,0))
            elif board[i][j] == "G":
                g = [i,j]
    
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    while q:
        y, x, cnt = q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if nx < 0 or nx >= c or ny < 0 or ny >= r or board[ny][nx] == "D":
                    continue
            while True:
                nny = dy[i] + ny
                nnx = dx[i] + nx
                if nnx < 0 or nnx >= c or nny < 0 or nny >= r or board[nny][nnx] == "D":
                    break
                ny = nny
                nx = nnx
            if matrix[ny][nx] == -1:
                matrix[ny][nx] = cnt+1
                q.append((ny, nx, cnt+1))
            
    answer = matrix[g[0]][g[1]]
    return answer