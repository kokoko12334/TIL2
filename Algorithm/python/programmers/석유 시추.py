import sys
sys.setrecursionlimit(10**8)
from collections import defaultdict
def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    seen = [[0]*m for _ in range(n)]
    g = 1
    group = defaultdict(int)
    def dfs(y,x,g):
        
        if seen[y][x] or land[y][x] == 0:
            return g
        seen[y][x] = g
        group[g] += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 > nx or nx >= m or 0 > ny or ny >= n:
                continue
            dfs(ny,nx,g)
        
        return g + 1
        
    for i in range(n):
        for j in range(m):
            g = dfs(i,j,g)
    
    for i in range(m):
        summ = 0
        visited = set()
        for j in range(n):
            if not seen[j][i]:
                continue
            g = seen[j][i]
            if g not in visited:
                summ += group[g]
                visited.add(g)
                
        answer = max(summ, answer)
    return answer