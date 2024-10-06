def solution(game_board, table):
    answer = -1
    n = len(game_board)
    space = []
    seen = [[0] * n for _ in range(n)]
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    
    for init_y in range(n):
        for init_x in range(n):
            if seen[init_y][init_x]:
                continue
            if game_board[init_y][init_x]:
                seen[init_y][init_x] = 1
                continue
            arr = []
            stack = [(init_y, init_x)]
            seen[init_y][init_x] = 1
            while stack:
                y,x = stack.pop()
                arr.append([y,x])
                for i in range(4):
                    ny = dy[i] + y
                    nx = dx[i] + x
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if game_board[ny][nx]:
                        seen[ny][nx] = 1
                        continue
                    if not seen[ny][nx]:
                        seen[ny][nx] = 1
                        stack.append((ny, nx))
            space.append(arr)
    
    for arr in space:
        y_min = min([i[0] for i in arr])
        x_min = min([i[1] for i in arr]) 
        for i in range(len(arr)):
            arr[i][0] -= y_min
            arr[i][1] -= x_min
        arr.sort()
    
    puzzle = []
    seen = [[0] * n for _ in range(n)]
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    
    for init_y in range(n):
        for init_x in range(n):
            if seen[init_y][init_x]:
                continue
            if not table[init_y][init_x]:
                seen[init_y][init_x] = 1
                continue
            arr = []
            stack = [(init_y, init_x)]
            seen[init_y][init_x] = 1
            while stack:
                y,x = stack.pop()
                arr.append([y,x])
                for i in range(4):
                    ny = dy[i] + y
                    nx = dx[i] + x
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if not table[ny][nx]:
                        seen[ny][nx] = 1
                        continue
                    if not seen[ny][nx]:
                        seen[ny][nx] = 1
                        stack.append((ny, nx))
            puzzle.append(arr)
            
    for arr in puzzle:
        y_min = min([i[0] for i in arr])
        x_min = min([i[1] for i in arr]) 
        for i in range(len(arr)):
            arr[i][0] -= y_min
            arr[i][1] -= x_min
        arr.sort()

    puzzle = {tuple(map(tuple, sublist)) for sublist in puzzle}
    space = {tuple(map(tuple, sublist)) for sublist in space}
    answer = 0
    
    def normalize(p):
        y_min = min(coord[0] for coord in p)
        x_min = min(coord[1] for coord in p)
        normalized_p = [(y - y_min, x - x_min) for y, x in p]
        normalized_p.sort()
        return tuple(normalized_p)
    
    def rotate_90(p):
        return [(y, n-1-x) for x, y in p]

    def rotate_180(p):
        return [(n-1-x, n-1-y) for x, y in p]
    
    def rotate_270(p):
        return [(n-1-y, x) for x, y in p]
    
    for p in puzzle:
        rotations = [p, normalize(rotate_90(p)), normalize(rotate_180(p)), normalize(rotate_270(p))]
        for rotated_p in rotations:
            if rotated_p in space:
                space.remove(rotated_p)
                answer += len(rotated_p)
                
                break
        
    return answer