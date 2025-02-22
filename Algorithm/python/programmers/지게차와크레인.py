def solution(storage, requests):
    
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    
    n = len(storage)
    m = len(storage[0])
    matrix = [[0] * m for _ in range(n)]
    
    for i in range(n):
        matrix[i][0] = -1
        matrix[i][m-1] = -1
    
    for i in range(m):
        matrix[0][i] = -1
        matrix[n-1][i] = -1
    
    def update_outside():
        nonlocal n, m
        stack = []
        seen = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == -2:
                    stack.append((i, j))
                    seen[i][j] = 1
        while stack:
            y, x = stack.pop()
            
            for i in range(4):
                ny = dy[i] + y
                nx = dx[i] + x
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                
                if seen[ny][nx]:
                    continue
                
                if matrix[ny][nx] == 0:
                    matrix[ny][nx] = -1
                    seen[ny][nx] = 1
                
                elif matrix[ny][nx] == -3:
                    matrix[ny][nx] = -2
                    seen[ny][nx] = 1
                    stack.append((ny, nx))
                
                
    def fork_lift(string):
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == -2 or matrix[i][j] == -3:
                    continue
                    
                if matrix[i][j] == -1 and storage[i][j] == string:
                    matrix[i][j] = -2
        
        update_outside()
        
    def crane(string):
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == -2 or matrix[i][j] == -3:
                    continue
                
                if matrix[i][j] == -1 and storage[i][j] == string:
                    matrix[i][j] = -2
                elif storage[i][j] == string:
                    matrix[i][j] = -3        
        update_outside()
        
    for i in range(len(requests)):
        string = requests[i]
        
        if len(string) == 1:
            fork_lift(string)
        else:
            crane(string[0])
        
        # print(f"#########{string}#####################")
        # for i in matrix:
        #     print(i)
    answer = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -2 or matrix[i][j] == -3:
                continue
            answer += 1
    return answer