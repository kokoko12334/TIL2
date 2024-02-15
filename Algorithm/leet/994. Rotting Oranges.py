from collections import deque

class Solution:
    def orangesRotting(self, grid) -> int:
        

        queue = deque()

        col = len(grid)
        row = len(grid[0])

        for i in range(col):
            for j in range(row):
                
                if grid[i][j] == 2:
                    queue.append([i,j,0])


        seen = [[0]*row for _ in range(col)]
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]

        answer = 0
        while queue:

            y,x,time = queue.popleft()
            
            seen[y][x] = 1
            answer = max(time,answer)

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= nx < row and 0 <= ny < col and seen[ny][nx] == 0 and grid[ny][nx] == 1:
                    
                    grid[ny][nx] = 2
                    queue.append([ny,nx,time+1])
        
        for i in range(col):
            for j in range(row):
                
                if seen[i][j] == 0 and grid[i][j] == 1:
                    return -1


        return answer