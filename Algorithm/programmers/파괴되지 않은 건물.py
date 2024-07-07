def solution(board, skill):
    n = len(board)
    m = len(board[0])
    
    delta = [[0] * (m+1) for _ in range(n+1) ]
    
    for s in skill:
        type_, r1, c1, r2, c2, degree = s 
        
        if type_ == 1:
            degree = -degree
        
        delta[r1][c1] += degree
        delta[r1][c2+1] += -degree
        delta[r2+1][c1] += -degree
        delta[r2+1][c2+1] += degree

    for i in range(n):
        for j in range(1, m):
            delta[i][j] += delta[i][j-1]

    for j in range(m):
        for i in range(1, n):
            delta[i][j] += delta[i-1][j]
    answer = 0
    for i in range(n):
        for j in range(m):
            board[i][j] += delta[i][j]
            if board[i][j] <= 0:
                answer += 1

    return (n * m) - answer