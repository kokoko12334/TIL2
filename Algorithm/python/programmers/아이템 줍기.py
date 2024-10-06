from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    
    matrix = [[0] *(101) for _ in range(101)]
    for i in rectangle:
        
        x1, y1, x2, y2 = [j * 2 for j in i]
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                matrix[x][y] = 1
    
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [1,0,-1,0,1,-1,1,-1]
    change = []
    for x in range(101):
        for y in range(101):
            if matrix[x][y] != 1:
                continue
            result = 0    
            for i in range(8):
                nx = dx[i] + x
                ny = dy[i] + y
            
                if nx < 0 or nx >= 101 or ny < 0 or ny >= 101:
                    continue
                if matrix[nx][ny] == 1:
                    result += 1
            if result == 8:
                change.append((x,y))
                
    for i in change:
        matrix[i[0]][i[1]] = 0
        
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]    
    seen = [[0] * 101 for _ in range(101)]
    q = deque([(characterX*2,characterY*2,0)])
    seen[characterX*2][characterY*2] = 1
    
    answer = 0
    
    while q:
        x, y, cnt = q.popleft()
        
        if x == itemX*2 and y == itemY*2:
            answer = cnt
            break
            
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if nx < 0 or nx >= 101 or ny < 0 or ny >= 101:
                continue
            
            if matrix[nx][ny] == 1 and not seen[nx][ny]:
                q.append((nx,ny,cnt + 1))
                seen[nx][ny] = 1

    return answer//2