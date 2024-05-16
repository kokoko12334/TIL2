from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(y,x,m,n):
            for i in range(4):
                ny = dy[i] + y
                nx = dx[i] + x
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if board[ny][nx] == "O" and (ny,nx) not in no_idx:
                    no_idx.add((ny,nx))
                    dfs(ny,nx,m,n)
        no_idx = set()
        m = len(board)
        n = len(board[0])
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]
        idx = [(0,i) for i in range(n)]
        idx += [(i,n-1) for i in range(1,m)]
        idx += [(m-1,i) for i in range(n-1)]
        idx += [(i,0) for i in range(m-1)]

        for i in idx:
            y,x = i
            if board[y][x] == "O":
                no_idx.add((y,x))
                dfs(y,x,m,n)        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i,j) not in no_idx:
                    board[i][j] = "X"
        