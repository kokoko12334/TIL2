class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        col = set()
        ne_diag = set()
        po_diag = set()

        arr = [['.']*n for _ in range(n)]
        answer = []
        def dfs(r):

            if r == n:
                answer.append(["".join(i) for i in arr])

            for c in range(n):
                ne = r - c
                po = r + c
                if not (c in col or ne in ne_diag or po in po_diag):
                    col.add(c)
                    ne_diag.add(ne)
                    po_diag.add(po)
                    arr[r][c] = 'Q'
                    dfs(r+1)
                    col.remove(c)
                    ne_diag.remove(ne)
                    po_diag.remove(po)
                    arr[r][c] = '.'
        dfs(0)
        return answer