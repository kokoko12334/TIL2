
from collections import deque
class Solution:
    def nearestExit(self, maze, entrance) -> int:
        
        row = len(maze)
        col = len(maze[0])
        q = deque()
        q.append(entrance+[0])

        seen = [[-1]*col for _ in range(row)]

        dy = [0,1,0,-1]
        dx = [1,0,-1,0]
        answer = -1
        seen[entrance[0]][entrance[1]] = 0
        while q:
            y,x,cnt = q.popleft()
            
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= nx < col and 0<=ny < row and seen[ny][nx] == -1 and maze[ny][nx] == ".":
                    
                    if nx == 0 or nx == col-1 or ny == 0 or ny == row-1:
                        answer = cnt+1
                        q = []
                        break

                    q.append([ny,nx,cnt+1])
                    seen[ny][nx] = cnt+1
                    
        return answer
    

# a = Solution()
# b=a.nearestExit(maze = [[".","+"]], entrance = [0,0]
# )

# print(b)