def solution(maze):
    n = len(maze)
    m = len(maze[0])
    blue = [[0] * m for _ in range(n)]
    red = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                red_idx = (i, j)
            elif maze[i][j] == 2:
                blue_idx = (i, j)
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    def dfs(y, x, arr, color):
        
        if color == 'red' and maze[y][x] == 3:
            red_path.append(arr[:])
            return
        if color == 'blue' and maze[y][x] == 4:
            blue_path.append(arr[:])
            return
        
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0 > nx or nx >= m or 0 > ny or ny >= n:
                continue
                
            if maze[ny][nx] == 5:
                continue
            
            if color == 'red':
                if red[ny][nx]:
                    continue
                red[ny][nx] = 1
                arr.append((ny,nx))
                dfs(ny, nx, arr, color)
                red[ny][nx] = 0
                arr.pop()
                
            elif color == 'blue':
                if blue[ny][nx]:
                    continue
                blue[ny][nx] = 1
                arr.append((ny,nx))
                dfs(ny, nx, arr, color)
                blue[ny][nx] = 0
                arr.pop()
            
    blue_path = []
    sy, sx = blue_idx
    blue[sy][sx] = 1
    dfs(sy, sx, [blue_idx], 'blue')
    
    red_path = []
    sy, sx = red_idx
    red[sy][sx] = 1
    dfs(sy, sx, [red_idx], 'red')
    answer = float('inf')
    for i in range(len(blue_path)):
        for j in range(len(red_path)):
            bp = blue_path[i]
            rp = red_path[j]
            # print(f"bp:{bp}, rp:{rp}")
            b_n = len(bp)
            r_n = len(rp)
            b_pointer = 0
            r_pointer = 0
            flag = True
            while b_pointer < b_n or r_pointer < r_n:
                if bp[b_pointer] == rp[r_pointer]:
                    flag = False
                    break
                if b_pointer < b_n - 1 and r_pointer < r_n - 1:
                    if bp[b_pointer + 1] == rp[r_pointer] and bp[b_pointer] == rp[r_pointer + 1]:
                        flag = False
                        break
                if b_pointer < b_n - 1:
                    b_pointer += 1
                if r_pointer < r_n - 1:
                    r_pointer += 1
                
                if b_pointer == b_n - 1 and r_pointer == r_n - 1:
                    break
            # print(f"결과:{flag}, b_pointer:{b_pointer}, r_porinter:{r_pointer}")
            if flag:
                answer = min(answer, max(b_pointer, r_pointer))
                
    if answer == float('inf'):
        answer = 0
        
    return answer