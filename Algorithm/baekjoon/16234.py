import sys
n, l, r = [int(i) for i in sys.stdin.readline().split()]

lst = []
for _ in range(n):
    lst.append([int(i) for i in sys.stdin.readline().split()])


al = set()
for i in range(n):
    for j in range(n):
        w = str(i)+ "." + str(j)
        al.add(w)
 

flag = True
go = True
answer = -1
dx = [1,0,-1,0]
dy = [0,1,0,-1]
summ = 0
while flag:
    if go:
        answer += 1
        go = False
        stack =  [[0,0]]
        seen = [[False]*n for _ in range(n)]
        seen[0][0] = True
        aliance = [[0,0]]
        summ  = lst[0][0]
        
        while stack:
            out = stack.pop()
            
            y,x = out[0], out[1]
           
            
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if nx < 0 or nx >= n or ny <0 or ny >= n:
                    continue
                
                if l <= abs(lst[ny][nx] - lst[y][x]) <=r and not seen[ny][nx]:

                    stack.append([ny, nx])
                    seen[ny][nx] = True
                    aliance.append([ny, nx])
                    summ += lst[ny][nx]
            if not stack:
                total = len(aliance)
                if len(aliance) >= 2:
                   
                    new = int(summ/total)
                    for i in aliance:
                        y, x = i[0], i[1]
                        lst[y][x] = new
                    go = True
                ko = True
                for i in range(n):
                    if ko:
                        for j in range(n):
                            if seen[i][j] == False:
                                next = [i,j]
                                stack.append(next)
                                seen[i][j] = True
                                aliance = [next]
                                summ = lst[i][j]
                                ko = False
                                break
           

    if not go:
        break

print(answer)
