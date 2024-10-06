from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n = len(board)
        m = len(board[0])
        k = len(word)
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]

        def dfs(y,x,k,level):
            if seen[y][x]:
                return
            if arr[-1] != word[level]:
                return
            if len(arr) == k:
                # print(arr,y,x)
                if "".join(arr) == word:
                    return True
                return

            flag = False
            seen[y][x] = 1
            for i in range(4):
                ny = dy[i] + y
                nx = dx[i] + x
                if 0 > nx or nx >= len(board[0]) or 0 > ny or ny >= len(board):
                    continue
                arr.append(board[ny][nx])
                flag = dfs(ny,nx,k,level+1)
                if flag:
                    return True
                arr.pop()
            seen[y][x] = 0

        arr = []
        seen = [[0]*m for _ in range(n)]
        flag = False
        
        for i in range(n):
            for j in range(m):
                level = 0
                arr.append(board[i][j])
                flag = dfs(i,j,k,level)
                arr.pop()
                if flag:
                    return True
        
        return False









