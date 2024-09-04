def solution(n):
    
    def dfs(y, x, go, cnt):
        nonlocal answer
        
        if cnt == n:
            answer += 1
            return
        
        sett = set()
        for data in go:
            i, j = data
            if i < y:
                continue
            if i == y and j <= x:
                continue
            if i == y or j == x or abs(y-i) == abs(x-j):
                continue
            sett.add((i, j))
        
        
        for next_node in sett:
            dfs(next_node[0], next_node[1], sett, cnt+1)
            
        
        return 
        
    init = set()
    answer = 0
    for i in range(n):
        for j in range(n):
            init.add((i,j))
    for i in range(n):
        for j in range(n):
            dfs(i, j, init , 1)
    return answer






def solution(n):
    
    board = [-1] * n
    answer = [0]

    def backtracking(depth):
        if depth == n:
            answer[0] += 1
            return

        for i in range(n):
            board[depth] = i
            if is_valid(depth):
                backtracking(depth + 1)

    def is_valid(i):
        for j in range(i):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                return False
        return True

    backtracking(0)
    return answer[0]