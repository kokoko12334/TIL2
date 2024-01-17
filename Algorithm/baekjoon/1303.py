import sys
#n 가로 m 세로
#lst[m][n]
n, m = [int(i) for i in sys.stdin.readline().split()]

g = []
seen = []
for _ in range(m):
    g.append(sys.stdin.readline())
    seen.append([False]*n)
#stack[컬러][지표]

stack = [[g[0][0], [0,0]]]
seen[0][0] = True

dx = [1,0,-1,0]
dy = [0,1,0,-1]
score = {"W":0 , "B": 0}
cnt = 0
while stack:
    
    out = stack.pop()
    cnt += 1
    y = out[1][0]
    x = out[1][1]
    color = out[0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <0 or nx>=n or ny <0 or ny >= m:
            continue
        if g[ny][nx] == color and seen[ny][nx] == False:
            stack.append([g[ny][nx], [ny,nx]])
            seen[ny][nx] = True

    if not stack:
        
        score[color] += (cnt)**2
        cnt = 0
        go = True
        for i in range(m):
            if go:
                for j in range(n):
                    if seen[i][j] == False:
                        stack.append([g[i][j], [i,j]])
                        seen[i][j] = True
                        go = False
                        break

print(score['W'], score['B'])
