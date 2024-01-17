import sys
sys.setrecursionlimit(10**6)
n = int(input())

lst_normal = [input() for _ in range(n)]

lst_non = [i.replace("G", "R") for i in lst_normal]

col = n
row = len(lst_normal[0])
dx = [1,0,-1,0]
dy = [0,1,0,-1]



def dfs(lst):
    global cnt

    if stack:
        out = stack.pop()
        y = out[1][0]
        x = out[1][1]
        color = out[0]
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx <0 or nx>= row or ny <0 or ny >= col:
                continue

            if lst[ny][nx] == color and not seen[ny][nx]:
                stack.append([lst[ny][nx], [ny,nx]])
                seen[ny][nx] = True
        
        if not stack:
            cnt += 1 
            stop = False
            for i in range(len(seen)):
                if stop:
                    break
                for j in range(len(seen[i])):
                    if seen[i][j] == False:
                        stack.append([lst[i][j],[i,j]])
                        seen[i][j] = True
                        stop = True
                        break
        
        dfs(lst)

answer = []

stack = [[lst_normal[0][0], [0,0]]]
seen = [[False]*row for i in range(col)]
seen[0][0] = True
cnt = 0
dfs(lst_normal)
answer.append(cnt)
#################
stack = [[lst_non[0][0], [0,0]]]
seen = [[False]*row for i in range(col)]
seen[0][0] = True

cnt = 0
dfs(lst_non)
answer.append(cnt)


print(*answer)