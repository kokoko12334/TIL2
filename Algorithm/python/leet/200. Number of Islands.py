from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])        
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]

        def dfs(y,x,n,m):
            
            if 0 > x or x >= m or 0 > y  or y >= n or grid[y][x] == "0":
                return
            grid[y][x] = "0" 
            for idx in range(4):
                dfs(y + dy[idx], x + dx[idx],n,m)

            
        answer = 0
        for y in range(n):
            for x in range(m):
                if grid[y][x] == "1":
                    answer += 1
                    dfs(y,x,n,m)
        

        return answer
    