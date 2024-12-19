from collections import deque
def solution(maps):
    row = len(maps)
    col = len(maps[0])
    
    for i in range(row):
        for j in range(col):
            if maps[i][j] == "S":
                s = (i, j)
            elif maps[i][j] == "L":
                l = (i, j)
            elif maps[i][j] == "E":
                e = (i, j)
    def bfs(s, e):
        
        nonlocal row, col
        
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]
        sy, sx = s
        ey, ex = e
        q = deque([(sy, sx, 0)])
        seen = [[-1] * col for _ in range(row)]
        seen[sy][sx] = 0
        
        while q:
            y, x, cnt = q.popleft()
            for i in range(4):
                ny = dy[i] + y
                nx = dx[i] + x
                if nx < 0 or nx >= col or ny < 0 or ny >= row:
                    continue
                if maps[ny][nx] == "X":
                    continue
                if seen[ny][nx] != -1:
                    continue
                
                seen[ny][nx] = cnt + 1
                q.append((ny, nx, cnt + 1))
        
        return seen[ey][ex] 
    
    answer = 0
    result1 = bfs(s, l)
    result2 = bfs(l, e)
    if result1 == -1 or result2 == -1:
        return -1
    answer += result1
    answer += result2
    return answer