class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def next_level(y,x,res):
            no = set()
            for i in range(n):
                no.add((y,i))
                no.add((i,x))
            
            s_y, s_x = y, x
            s_y -= 1
            s_x -= 1
            while s_y >=0 and s_x >= 0:
                no.add((s_y,s_x))
                s_y -= 1
                s_x -= 1

            s_y, s_x = y, x
            s_y -= 1
            s_x += 1
            while s_y >=0 and s_x < n:
                no.add((s_y,s_x))
                s_y -= 1
                s_x += 1

            s_y, s_x = y, x
            s_y += 1
            s_x += 1
            while s_y < n and s_x < n:
                no.add((s_y,s_x))
                s_y += 1
                s_x += 1
            
            s_y, s_x = y, x
            s_y += 1
            s_x -= 1
            while s_y < n and s_x >= 0:
                no.add((s_y,s_x))
                s_y += 1
                s_x -= 1
            new_res = res - no

            return new_res

        answer = []
        arr = []
        def dfs(y,x,level,res):

            if seen[y][x]:
                return
            
            seen[y][x] = 1
            if level == n:
                answer.append(1)
                arr.append((y,x))
                return

            new_res = next_level(y,x,res)
            child = res & new_res
            # print(f"인덱스:{y,x}, child:{child}, level:{level}")
            for c in child:
                ny,nx = c
                # print(f"c:{ny,nx}")
                dfs(ny,nx,level+1,child)

            seen[y][x] = 0
        seen = [[0]*n for _ in range(n)]
        res = {(k,o) for k in range(n) for o in range(n)}
        for i in range(n):
            for j in range(n):
                dfs(i,j,1,res)
                
        # print(answer)
        return sum(answer)