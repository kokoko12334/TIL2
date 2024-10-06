from collections import deque
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #m: x , n: y
        if obstacleGrid[-1][-1] or obstacleGrid[0][0]:
            return 0
        m = len(obstacleGrid[0])
        n  = len(obstacleGrid)
        dx = [1,0]
        dy = [0,1]
        
        dp = [[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j]:
                    dp[i][j] = -1
        
        q = deque()
        q.append([0,0])

        dp[0][0] = 1
        while q:
            y,x = q.popleft()
            for i in range(2):
                ny = dy[i] + y
                nx = dx[i] + x
                if nx >=m or nx < 0 or ny >=n or ny < 0:
                    continue
                
                if dp[ny][nx] == 0:
                    if 0 <= nx-1 < m and dp[ny][nx-1] != -1:
                        dp[ny][nx] += dp[ny][nx-1]
                    if 0 <= ny-1 < n and dp[ny-1][nx] != -1:
                        dp[ny][nx] += dp[ny-1][nx]
                    q.append([ny,nx])
        
        if dp[-1][-1] > 0:
            return dp[-1][-1]
        
        return 0