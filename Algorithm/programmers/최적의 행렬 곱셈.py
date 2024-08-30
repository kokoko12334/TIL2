from collections import defaultdict
def solution(matrix_sizes):
    n = len(matrix_sizes)
    g = defaultdict(list)
    stack = []
    for i in range(n):
        r = matrix_sizes[i][1]
        flag = False
        for j in range(n):
            if i == j:
                continue
            if r == matrix_sizes[j][0]:
                g[r].append(j)
                flag = True
        if flag:
            stack.append(matrix_sizes[i])
    print(g)
    seen = [0] * n
    def dfs(m, cnt, summ):
        print(f"matrix:{m}, cnt:{cnt}, summ:{summ}")
        if cnt == n:
            return summ
        print(g[m[1]])
        for i in g[m[1]]:
            if not seen[i]:
                seen[i] = 1
                m2 = matrix_sizes[i]
                summ += (m[0]*m[1]*m2[1])
                new_m = [m[0],m2[1]]
                dfs(new_m, cnt+1, summ)
                seen[i] = 0
    
    for m in stack:
        dfs(m, 1, 0)
        
        
    return 0