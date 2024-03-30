#10:00
from typing import List
#정답 => 뒤에 있는 칸을 중심으로 생각
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        #x:m , y:n
        m = len(matrix[0])
        n = len(matrix)
        
        k = min(m,n)

        dp = [[0]* m for _ in range(n)]
        
        answer = 0
        for i in range(n):
            for j in range(m):
                dp[i][j] = int(matrix[i][j])
                if matrix[i][j] == "1":
                    answer = 1
        
        for i in range(1,n):
            for j in range(1,m):
                if dp[i][j]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + dp[i][j]
                    answer = max(answer,dp[i][j])
        
        return answer*answer

#시간초과 난거 앞에 거 중심으로 생각함.
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        #x:m , y:n
        m = len(matrix[0])
        n = len(matrix)
        
        k = min(m,n)

        dp = []
        for i in range(k):
            arr = []
            for _ in range(n):
                arr.append([0]*m)                    
            dp.append(arr)
        
        answer = 0
        for i in range(n):
            for j in range(m):
                dp[0][i][j] = int(matrix[i][j])
                if int(matrix[i][j]):
                    answer = 1
        answer = 0
        for r in range(1,k):
            for i in range(n):
                for j in range(m):
                    v1, v2, v3, v4 = [0,0,0,0]
                    if dp[r-1][i][j]:
                        v1 = 1
                    if j+1 < m and dp[r-1][i][j+1]:
                        v2 = 1
                    if i+1 < n and dp[r-1][i+1][j]:
                        v3 = 1
                    if j+1 < m and i+1 < n and dp[r-1][i+1][j+1]:
                        v4 = 1
                    # print(f"num:{r} idx:{i,j}, v1:{v1},v2:{v2},v3:{v3},v4:{v4}")
                    summ = v1+v2+v3+v4
                    if summ == 4:
                        dp[r][i][j] = 1
                        result = (r+1) * (r+1)
                        answer = max(answer,result)
                    else:
                        dp[r][i][j] = 0

        return answer