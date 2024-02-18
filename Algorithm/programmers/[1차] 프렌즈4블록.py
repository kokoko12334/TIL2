def check(b,m,n):
    
    result = 0
    idx_info = [[i]*n for i in range(m)]
    
    dy = [0,1,1]
    dx = [1,1,0]
    remove = set()
    for y in range(m):
        for x in range(n):
            string = b[y][x]
            if string == None:
                continue
            cnt = 0
            arr = [(y,x)]
            for i in range(3):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= nx < n and 0 <= ny < m and b[ny][nx] == string:
                    cnt += 1
                    arr.append((ny,nx))
            if cnt == 3:
                for i in arr:
                    if i not in remove:
                        remove.add(i)
                        
                        result += 1
    for i in remove:
        y,x = i
        
        for j in range(y):
            
            idx_info[j][x] += 1
            
    new_b = [[None]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if (i,j) not in remove:
                ny,nx = idx_info[i][j],j
                
                new_b[ny][nx] = b[i][j]
                
    return result, new_b

#m: 높이,y, col,  n: 폭,x,row
def solution(m, n, board):
    answer = 0
    result,nb = check(board,m,n)
    answer += result
    while result != 0:
        result,nb = check(nb,m,n)
        answer += result
    
    return answer