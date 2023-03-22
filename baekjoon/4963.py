
#w:가로x h:세로y
while True:
    w,h = [int(i) for i in input().split()]
    if w == 0 and h == 0:
        break
    
    lst = []

    for _ in range(h):
        lst.append([int(i) for i in input().split()])

    dx = [1,0,-1,0,1,1,-1,-1]
    dy = [0,1,0,-1,-1,1,1,-1]

    
    one = []
    for i in range(h):
        for j in range(w):
            if lst[i][j] == 1:
                one.append([i,j])
    answer = 0            
    if one:
        stack = [one[0]]

        seen = [[False]*w for _ in range(h)]
        seen[one[0][0]][one[0][1]] = True

        while stack:
            out = stack.pop()
            
            y = out[0]
            x = out[1]
            for i in range(8):
                ny = dy[i] + y
                nx = dx[i] + x
                if nx <0 or nx >= w or ny <0 or ny >=h:
                    continue
                
                if lst[ny][nx] == 1 and seen[ny][nx] == False:
                    stack.append([ny,nx])
                    seen[ny][nx] = True


            if not stack:
                answer += 1
                for i in range(len(one)):
                    y = one[i][0]
                    x = one[i][1]
                    if seen[y][x] == False:
                        stack.append([y,x])
                        seen[y][x] = True
                        break 
        print(answer)
    else:
        print(0)



