# row - col => 양의 대각선으로 행과 열의 차이 가 일정하면 같은 대각선
# ro + col => 음의 대각선
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row):
            if row == n:
                return 1
            solutions = 0
            for col in range(n):
                if col in cols or (row - col) in pos_diags or (row + col) in neg_diags:
                    continue
                
                cols.add(col)
                pos_diags.add(row - col)
                neg_diags.add(row + col)
                
                solutions += backtrack(row + 1)
                
                cols.remove(col)
                pos_diags.remove(row - col)
                neg_diags.remove(row + col)
                
            return solutions
        
        cols = set()
        pos_diags = set()
        neg_diags = set()
        
        return backtrack(0)