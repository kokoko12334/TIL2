from collections import deque
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #m: col , n:row

        dp = [[0]*n for _ in range(m)]

        dp[0][0] = 1

        dy = [0,1]
        dx = [1,0]

        q = deque()
        q.append([0,0])
        
        while q:
            y,x = q.popleft()
            
            for i in range(2):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= nx < n and 0<= ny < m:
                    if dp[ny][nx] == 0:
                        if 0 <= nx-1 <n:
                            dp[ny][nx] += dp[ny][nx-1]
                        if 0 <= ny-1 <m:
                            dp[ny][nx] += dp[ny-1][nx]
                        q.append([ny,nx])
                        
        answer = dp[m-1][n-1]
        return answer
