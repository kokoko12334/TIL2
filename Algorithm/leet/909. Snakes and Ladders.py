from collections import deque
from typing import List
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)
        tables = {}
        cnt = 1
        num = 1
        for i in range(n-1,-1,-1):
            if cnt%2:
                for j in range(n):
                    tables[num] = (i,j)
                    num += 1
            else:
                for j in range(n-1,-1,-1):
                    tables[num] = (i,j)
                    num += 1
            cnt += 1

        q = deque()
        q.append((1,0))
        seen = set()
        double_arr = [[-1]*n for _ in range(n)]
        while q:
            num, cnt = q.popleft()
            if num in seen:
                continue
            
            seen.add(num)
            y,x = tables[num]
            double_arr[y][x] = cnt
            for i in range(1, 7):
                next_num = num + i
                if next_num > (n**2):
                    break
                ny,nx = tables[next_num]
                if board[ny][nx] != -1:
                    q.append((board[ny][nx], cnt+1))
                else:
                    q.append((next_num, cnt+1))

        y,x = tables[n**2]
        
        return double_arr[y][x]