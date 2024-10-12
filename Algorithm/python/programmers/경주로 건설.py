from collections import deque
def solution(board):
    n = len(board)
    seen = [[float('inf')] * n for _ in range(n)]
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    
    q = deque([(0,0,0,-1,(0,0))])
    seen[0][0] = 0
    while q:
        y, x, cnt, cor, go = q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[ny][nx] == 1:
                continue
            go2 = (abs(ny-y), abs(nx-x))
            cor2 = cor
            if go2 != go:
                cor2 += 1
            
            price = (cnt+1) * 100 + cor2 * 500
            if seen[ny][nx] < price:
                continue
            
            seen[ny][nx] = price
            q.append((ny,nx,cnt+1,cor2,go2))
    
    return seen[-1][-1]