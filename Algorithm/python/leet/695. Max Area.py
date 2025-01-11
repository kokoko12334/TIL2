from typing import List
from collections import defaultdict
class Solution:

    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]

        row = len(grid)
        col = len(grid[0])
        seen = [[0] * col for _ in range(row)]
        
        stack = []
        num = 1
        for r in range(row):
            for c in range(col):
                if grid[r][c]:
                    stack.append((r, c, num))
                    num += 1
        dic = defaultdict(int)

        while stack:
            r, c, num = stack.pop()
            if seen[r][c] == 1:
                continue

            seen[r][c] = 1
            dic[num] += 1
            for i in range(4):
                ny = dy[i] + r
                nx = dx[i] + c

                if nx < 0 or nx >= col or ny < 0 or ny >= row:
                    continue
            
                if grid[ny][nx] == 0 or seen[ny][nx]:
                    continue
                
                stack.append((ny, nx, num))

        answer = 0
        for v in dic.values():
            answer = max(answer, v)
        return answer