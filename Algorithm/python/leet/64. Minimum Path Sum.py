from collections import deque
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #x:m y:n
        m = len(grid[0])
        n = len(grid)
        dx = [1,0]
        dy = [0,1]

        q = deque()
        q.append([0,0])
        dp = [[0]*m for _ in range(n)]
        dp[0][0] = grid[0][0]
        while q:
            y,x = q.popleft()
            for i in range(2):
                ny = dy[i] + y
                nx = dx[i] + x
                if nx >= m or nx < 0 or ny >= n or ny < 0:
                    continue
                v1 = float("inf")
                v2 = float("inf")
                if dp[ny][nx] == 0:
                    if 0 <= nx-1 < m:
                        v1 = dp[ny][nx-1]
                    if 0 <= ny-1 < n:
                        v2 = dp[ny-1][nx]
                    dp[ny][nx] = min(v1,v2) + grid[ny][nx]
                    q.append([ny,nx])
        
        # for i in dp:
        #     print(i)

        return dp[-1][-1]