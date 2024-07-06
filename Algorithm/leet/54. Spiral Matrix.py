from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        n = len(matrix)
        m = len(matrix[0])
        seen = [[0] * m for _ in range(n)]

        d_info = {'right': [0, 1], 'down':[1, 0], 'left':[0, -1], 'up':[-1, 0]}

        def dfs(y, x, d):
            answer.append(matrix[y][x])
            seen[y][x] = 1
            # print(f"현재지점:{y,x} 갈방향:{d}")
            dy, dx = d_info[d]
            ny = y + dy
            nx = x + dx
            # print(f"갈방향 지점:{ny,nx}")
            if nx < 0 or nx >= m or ny < 0 or ny >= n or seen[ny][nx]:
                if d == 'right':
                    d = 'down'
                    dy, dx = d_info[d]
                    ny = y + dy
                    nx = x + dx
                elif d == 'down':
                    d = 'left'
                    dy, dx = d_info[d]
                    ny = y + dy
                    nx = x + dx
                elif d == 'left':
                    d = 'up'
                    dy, dx = d_info[d]
                    ny = y + dy
                    nx = x + dx
                elif d == 'up':
                    d = 'right'
                    dy, dx = d_info[d]
                    ny = y + dy
                    nx = x + dx
            # print(f"수정 후:{ny,nx} 방향:{d}")
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n or seen[ny][nx]:
                return
            
            dfs(ny, nx, d)

        dfs(0,0,'right')
        return answer       