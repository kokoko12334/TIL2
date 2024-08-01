from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        

        m = len(board)
        n = len(board[0])

        dy = [0,1,1,1,0,-1,-1,-1]
        dx = [1,1,0,-1,-1,-1,0,1]
        live = []
        die = []
        for y in range(m):
            for x in range(n):
                one = 0
                zero = 0
                for i in range(8):
                    ny = dy[i] + y
                    nx = dx[i] + x
                    if 0 > nx or n <= nx or 0 > ny or m <= ny:
                        continue
                    if board[ny][nx]:
                        one += 1
                    else:
                        zero += 1
                
                if board[y][x]:
                    if one == 2 or one == 3:
                        live.append((y,x))
                    else:
                        die.append((y,x))
                else:
                    if one == 3:
                        live.append((y,x))
                    else:
                        die.append((y,x))

        for i in live:
            y, x = i
            board[y][x] = 1
        for i in die:
            y, x = i
            board[y][x] = 0