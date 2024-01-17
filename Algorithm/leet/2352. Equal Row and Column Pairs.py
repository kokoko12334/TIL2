class Solution:
    def equalPairs(self, grid) -> int:
        
        answer = 0
        n = len(grid)
        cols = []
        for i in range(n):
            arr = []
            for j in range(n):
                arr.append(grid[j][i])
            cols.append(arr)
        
        for i in range(n):
            row = str(grid[i])
            for j in range(n):
                col = cols[j]
                
                if row == str(col):
                    answer += 1

        return answer